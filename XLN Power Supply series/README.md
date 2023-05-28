# BK Precision XLN High Power Programmable DC Power Supplies
These python scripts are for the BK XLN Series High Power Programmable DC Power Supplies


  
### Models
Models: XLN3640, XLN6024, XLN8018, XLN10014, XLN15010, XLN30052, XLN60026


### Documentation
Manual: [Series Manual](https://bkpmedia.s3.amazonaws.com/downloads/manuals/en-us/XLN_manual.pdf)
  
Data Sheet: [Series Data Sheet](https://bkpmedia.s3.amazonaws.com/downloads/datasheets/en-us/XLN_datasheet.pdf)

### Script Usage
<br>
The following steps must be done before using these scripts: 

1) Identify the serial port name of your instrument. On Windows, this is a ```COMxx``` port name. On MacOS, this is ```/dev/tty.usbserial-{sernum}```, where ```{sernum}``` is the serial number of the XLN power supply.
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

### Operating Tips for the XLN Series
<br>
Whenever a remote command is received from the serial port, the XLN power supply enters REMOTE MODE, and the front display indicates __RMT__ in the lower-right corner. <br>
The frontal keyboard is LOCKED in RMT mode, and the user cannot access any local function. <br>
To restore local control, you need to press the __decimal point key__ ```[.]```, which unlocks the keypad. 

