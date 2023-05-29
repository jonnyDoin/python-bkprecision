###################################################################################################
#   LIST_PORTS - LIST ALL SERIAL PORTS IN THE SYSTEM
#   ------------------------------------------------
#
#   This is a helper script to find the correct serial port name for a BK XLN power supply.
#   
#   The XLN series have a Silicon Labs CP1202 Serial to USB bridge, and enumerate as a serial port. 
#   On Windows, it will enumerate as a 'COMxx' port name.
#   On MacOSX, it will enumerate as a '/dev/tty.usbserial-<serial_number>', where <serial_number> 
#   is the equipment serial number. This naming scheme allows multiple XLN units to be connected to the
#   same computer, and to be correctly identified.
#   
#   This script lists all current serial ports in the system. 
# 
#--------------------------------------------------------------------------------------------------
#   DESCRIPTION
#   -----------
# 
#   The program lists all serial ports. 
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
from serial.tools import list_ports as lp

script_ver = "v1.0.2"

print()
print('LIST PORTS ', script_ver)
print('----------------------------------------------')

for com in lp.comports():
    print(com.device)
    print("\tname:\t\t", com.name)
    if (com.description != "n/a"):  print("\tdescription:\t", com.description)
    if (com.hwid != "n/a"):         print("\thwid:\t\t", com.hwid)
    if (com.vid != None):           print("\tvid:\t\t", com.vid)
    if (com.pid != None):           print("\tpid:\t\t", com.pid)
    if (com.serial_number != None): print("\tserial_number:\t", com.serial_number)
    if (com.location != None):      print("\tlocation:\t", com.location)
    if (com.manufacturer != None):  print("\tmanufacturer:\t", com.manufacturer)
    if (com.product != None):       print("\tproduct:\t", com.product)
    if (com.interface != None):     print("\tinterface:\t", com.interface)
