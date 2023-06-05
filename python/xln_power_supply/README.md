# BK Precision XLN High Power Programmable DC Power Supplies
These python scripts are for the BK XLN Series High Power Programmable DC Power Supplies

<br>
 
## Models
Models: XLN3640, XLN6024, XLN8018, XLN10014, XLN15010, XLN30052, XLN60026

<br>

## Documentation
XLN Manual: [Series Manual](/docs/datasheets/XLN_Series_manual.pdf) <br>
XLN Programming Manual: [Programming Manual](/docs/datasheets/BK%20Precision%208600_Series_programming_manual.pdf) <br>
XLN Data Sheet: [Series Data Sheet](/docs/datasheets/XLN_Series_datasheet.pdf) <br>
Serial-to-USB Bridge: [CP1202](/docs/datasheets/CP2102-9.pdf) <br>

<br>

## Serial Port Configuration

The XLN power supplies have the following configuration:

```python
bk.baudrate=57600
bk.bytesize=8
bk.parity='N'
bk.stopbits=1
bk.xonxoff=False
bk.rtscts=False
bk.dsrdtr=False
```

The above settings are the default settings for the ```pyserial``` module, except the baudrate, which is ```9600baud```. You have to use ```57600baud``` with the XLN power supplies.

<br>

## Scripts Usage
The following steps must be done before using these scripts: 

1) Identify the serial port name of your instrument. On Windows, this is a ```COMxx``` port name. On MacOS, this is ```/dev/tty.usbserial-{sernum}```, where ```{sernum}``` is the serial number of the XLN power supply. You can use the script [list_ports.py](../list_ports.py) to list all serial port devices in your system, and identify the correct Silicon Labs [CP1202](/docs/datasheets/CP2102-9.pdf) USB Bridge device port to use.
2) Set the ```portname``` variable to your instrument serial port name.
3) Change the ```model_id``` variable to your XLN power supply model. 

```python
import serial
import time

script_ver = "v1.0.0"
model_id = b'XLN3640'                       # change the model_id to your XLN model
portname = '/dev/tty.usbserial-275K22178'   # change the device port name for your device name!
                                            # on windows use 'COMxx'

```

4) The XLN power supplies use an internal serial-to-USB bridge chip (CP1202), that is bus-powered by the USB cable. This means that even when the power supply is unpowered, or when the internal processor is unresponsive, the serial port will be normally enumerated and opened. This requires another level of authentication before starting sending commands to the XLN power supply. We verify that the MODEL string returned by the instrument matches the expected ```model_id``` string, and issue and error when it fails to return the correct model string. 

<br>

## Scripts included in this folder

- [xln_id.py](./xln_id.py) — retrieves ID info of the connected XLN power supply
- [xln_clr_pgm.py](./xln_clr_pgm.py) — clears all internal stored programs
- [xln_gen_pgm.py](./xln_gen_pgm.py) — generates a staircase waveform in PROG1
- [xln_gen_pgm_sine.py](./xln_gen_pgm_sine.py) — generates a sinewave burst waveform in PROG1
- [xln_run_pgm.py](./xln_run_pgm.py) — executes the program stored at PROG1
- [xln_wave.py](./xln_wave.py) — generate a staircase waveform and display realtime voltage and current


<br>

## Operating Tips for the XLN Series
Whenever a remote command is received from the serial port, the XLN power supply enters REMOTE MODE, and the front display indicates __RMT__ in the lower-right corner. 

The frontal keyboard is LOCKED in RMT mode, and the user cannot access any local function. 

To restore local control, you need to press the __decimal point key__  ```[.]```  which unlocks the keypad. 

---

<br>

