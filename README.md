# CISTEK / B&amp;K Precision Python Remote Control

This repository contains python example scripts for remote programming of B&K Precision instruments.

It is developed by GridVortex Systems for [CISTEK Equipamentos].

The repo has code examples for several instrument families, and general information and documentation for each family.


## Objectives 

The main purpose of this project is to provide simple examples to get users started with python and SCPI remote commands for test and measurement automation with B&K Precision instruments. 

Also shown are techniques to obtain realtime plotting of remote measurement from BK Instruments, to achieve better measurement automation results, and integration of multiple instruments in a simple python programming environment. 

The techniques exemplified in the scripts are not exclusive to BK instruments, and can be generally applied to many other instruments, but specific sequences and commands are specific to each family or model. All scripts here are tested in real B&K Precision instruments. 

<br>
Always read the manufacturers programming manual for the set of SCPI and proprietary commands supported by the instrument. 

<br>

## Documentation
XLN Power Supply Manual: [Series Manual](/docs/datasheets/XLN_Series_manual.pdf) <br>
XLN Power Supply Data Sheet: [Series Data Sheet](/docs/datasheets/XLN_Series_datasheet.pdf) <br>
Serial-to-USB Bridge: [CP1202](/docs/datasheets/CP2102-9.pdf) <br>
BK 8600 Electronic Load Programming Manual: [Programming Manual](/docs/datasheets/BK%20Precision%208600_Series_programming_manual.pdf) <br>

<br>

## CODE

The code examples are in the [XLN examples](/python/xln_power_supply/) folder. Please read the [README](/python/xln_power_supply/README.md) for details on the code examples.

- [xln_id.py](/python/xln_power_supply/xln_id.py) — retrieves ID info of the connected XLN power supply
- [xln_clr_pgm.py](/python/xln_power_supply/xln_clr_pgm.py) — clears all internal stored programs
- [xln_gen_pgm.py](/python/xln_power_supply/xln_gen_pgm.py) — generates a staircase waveform in PROG1
- [xln_gen_pgm_sine.py](/python/xln_power_supply/xln_gen_pgm_sine.py) — generates a sinewave burst waveform in PROG1
- [xln_run_pgm.py](/python/xln_power_supply/xln_run_pgm.py) — executes the program stored at PROG1
- [xln_wave.py](/python/xln_power_supply/xln_wave.py) — generate a staircase waveform and display realtime voltage and current
- [list_serial_ports.py](/python/xln_power_supply/list_serial_ports.py) – lists all USB serial ports (USB CDC) in the system. Use to find your serial port. The XLN series has a Silicon Labs CP1202 Serial to USB bridge.

## LICENSE

All example codes here are developed by Gridvortex and published as Open Source under a BSD 2-Clause License. <br>
Please read the License terms found in the [LICENSE] file in this repository. 

--- 

<br>

[CISTEK Equipamentos]: https://www.cistek.com.br/
[LICENSE]:./LICENSE
