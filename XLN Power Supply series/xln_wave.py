###################################################################################################
#   XLN_WAVE - REALTIME WAVEFORM PROGRAMMING OVER SCPI WITH OUTPUT VOLTAGE READBACK
#   -------------------------------------------------------------------------------
#
#   This is an example code to demonstrate the BK PRECISION XLN Programmable Power Supply Series. 
#   
#   The XLN series have a CP1202 Serial to USB bridge, and enumerate as a serial port. 
#   On Windows, it will enumerate as a 'COMxx' port name.
#   On MacOSX, it will enumerate as a '/dev/tty.usbserial-<serial_number>', where <serial_number> 
#   is the equipment serial number. This naming scheme allows multiple XLN units to be connected to the
#   same computer, and to be correctly identified.
#   
#   The example code uses the pyserial module, and SCPI commands to control the XLN power supply.
#   This is the basic sequence to talk to the power supply:
# 
#   1)  Identify the serial port device name. On Windows, it enumerates as a 'COMxx' virtual serial port. 
#       On MacOS, it enumerates as a tty.usbserial device, with name '/dev/tty.usbserial-<sernum>', where
#       <sernum> is the serial number of the XLN power supply. 
# 
#   2)  The communication uses the PySerial module API, to open the serial port and exchange ascii strings
#       with the power supply. All strings exchanged to/from the serial port are byte strings, and need to 
#       be byte encoded. 
# 
#   3)  The XLN series devices have a CP1202 Serial-to-USB Bridge chip, which is bus-powered. So, even when
#       the power supply is unpowered or unresponsive, the USB device port can be enumerated and opened. This
#       requires an positive identification from the power supply, before starting sending control commands. 
# 
#   4)  The power supply responds with its full device name to the '*IDN?' command, and also with the model and
#       version to the commands 'MODEL?' and 'VER?'. The serial number can also be read with the 'SYS:SER?' SCPI 
#       command. We use here the MODEL returned to validate a working device. 
#       NOTE:   If the power supply is connected and powered up, but is not responding to any identification commands,
#               it might be necessary to do a manual power OFF/ON on the power supply. 
# 
#   5)  Some commands do not need a response, but a few commands are query/response commands, and need to have the 
#       response read, even if it will be discarded. 
# 
#   6)  The serial port must be closed at the end of the program, to avoid a locked port in some operating systems. 
# 
#--------------------------------------------------------------------------------------------------
#   DESCRIPTION
#   -----------
# 
#   The program opens the serial port, authenticates the XLN power supply model, and sends the following sequence of
#   commands:
#       1) Turn the output ON
#       2) Send a sequence of stored voltage steps defined in an internal python list
#       3) Read the output voltage and display the voltage as a realtime plot
#       4) Turn the output OFF
#       5) Waits for the user to close the plot window
#       6) Close the serial port
# 
#--------------------------------------------------------------------------------------------------
#   THIS CODE IS CREATED BY GRIDVORTEX SYSTEMS FOR CISTEK EQUIPAMENTOS DE MEDICAO AS EXAMPLE CODE 
#   SUPPORT FOR CISTEK CUSTOMERS. THIS CODE IS PROVIDED AS IS, WITH NO IMPLIED OR EXPLICIT GUARANTEES
#   OF PERFORMANCE OR FUNCTIONALITY. 
#   NEITHER CISTEK NOR GRIDVORTEX ARE LIABLE FOR ANY DIRECT OR INDIRECT DAMAGES DERIVED FROM USE OF 
#   THIS CODE. 
#   THIS CODE IS PUBLISHED AS OPEN SOURCE FOR FREE USE. SUPPORT WILL BE PROVIDED ON GOODWILL, WITH NO 
#   OBLIGATION OF SUPPORT OR SERVICE BEING IMPLIED WITH THE PROVISION OF THIS CODE. 
#--------------------------------------------------------------------------------------------------
#   LICENSE:    BSD 2-CLAUSE LICENSE
#       
#               Copyright (c) 2023, by Jonny Doin, GridVortex Systems 
#               
#               Redistribution and use in source and binary forms, with or without
#               modification, are permitted provided that the following conditions are met:
#               
#               1. Redistributions of source code must retain the above copyright notice, this list 
#               of conditions and the following disclaimer.
#               
#               2. Redistributions in binary form must reproduce the above copyright notice, this 
#               list of conditions and the following disclaimer in the documentation and/or other 
#               materials provided with the distribution.
#               
#               THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
#               EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
#               OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
#               SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
#               INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED 
#               TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR 
#               BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
#               CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN 
#               ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH 
#               DAMAGE.
# 
###################################################################################################

import serial
import time
from math import ceil as ceil
import matplotlib.pyplot as plt

script_ver = "v1.0.1"
model_id = b'XLN3640'                       # change the model_id to your XLN model
portname = '/dev/tty.usbserial-275K22178'   # change the device port name for your device name!
                                            # on windows use 'COMxx'

# staircase waveform definition
vp = [0.0,  0.5,  1.0,  1.5,  2.0,  2.5,  3.0,  3.5,  4.0,  4.5,  5.0,  5.5,  6.0,  6.5,  7.0,  7.5,  8.0,  8.5,  9.0,  9.5, 10.0,  0.0,  0.0]
tp = [0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.0]

# plot setup
plt.ion()                                   # using matplotlib interactive mode for realtime update
fig = plt.figure(figsize=(6, 3))
x = [0]
y = [0]
ln, = plt.plot(x, y, '-')
plt.axis([0, 500, 0, 10])

cmd_vout = "SOUR:VOLT {}\r\n"

# plot realtime update function
def update_plt(yplot):
    x.append(x[-1] + 1)
    y.append(yplot)
    ln.set_data(x, y) 
    return ln,

def read_vout(instr):
    try:
        instr.write("VOUT?\r\n".encode())
        rd = instr.readline()
        # print('rd:', rd)
        vout = float(rd)
    except:
        vout = -1.0
    return vout
    
def write_cmd(instr, cmd, arg):
    _cmd = cmd.format(arg).encode()
    instr.write(_cmd)

def write_vout(instr, vout):
    write_cmd(instr, cmd_vout, vout)

def read_pause(instr, tpause):
    vout = -1
    pts = ceil(tpause / 0.080)
    for i in range(pts):
        vout = read_vout(instr)
        update_plt(vout)
        plt.pause(0.010)
    return vout

# instrument setup
print()
print('B&K PRECISION REMOTE CONTROL EXAMPLE BY CISTEK')
print('REALTIME WAVEFORM ', script_ver)
print('----------------------------------------------')
bk = serial.Serial()
bk.port = portname
bk.baudrate = 57600
bk.timeout = 0.2
bk.open()
if bk.is_open:
    print('Serial port OPEN')
    bk.reset_input_buffer()
    bk.reset_output_buffer()
    bk.write("\r\n".encode())               
    bk.write("*idn?\r\n".encode())          
    idn = bk.readline()                     
    bk.write("MODEL?\r\n".encode())
    model = bk.readline()                   
    bk.write("SYS:SER?\r\n".encode())          
    sernum = bk.readline()                  
    bk.write("VER?\r\n".encode())          
    version = bk.readline()
    print('Instrument ID:', idn)
    print('Instrument MODEL:', model)
    print('Instrument VERSION:', version)
    print('Instrument SN:', sernum)
    if model.find(model_id) != -1:
        bk.write("*cls\r\n".encode())
        # turn output ON
        bk.write("OUTP ON\r\n".encode())
        bk.write("OUTP?\r\n".encode())
        print("OUTP? : ", bk.readline())
        bk.write("STATUS?\r\n".encode())
        print("STATUS? : ", bk.readline())

        # draw initial figure
        plt.show(block=False)
        plt.pause(0.1)
        
        # generate the staircase ramp
        np = 0; vout = -1
        while tp[np] != 0.0:
            write_vout(bk, vp[np])
            vout = read_pause(bk, tp[np])
            print("Vout: ", vout)
            np = np + 1
        vout = read_pause(bk, 0.2)
        print("Vout: ", vout)
        bk.write("OUTP OFF\r\n".encode())
        print("OUTP OFF : ", bk.readline())
        plt.show(block=True)    # blocks until user closes plot window
    else:
        print('MODEL ID ERROR!')
    bk.close()
    print('Serial port CLOSED')
else:
    print('ERROR: serial.open() failed.')


