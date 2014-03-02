IP-Manipulator
==============

Small script to convert IP address between decimal, octal, and hex

If not explicitly declared with options, octal values must begin with '0' and hex values must begin with'0x' or '0X'

Usage: ./IP-Manipulator.py <ip_address> <options>

Options:

 -f or --file    :   output to a file with <filename>

       --dec     :   explicitly declare decimal input

       --hex     :   explicitly declare hexidecimal input

       --oct     :   explicitly declare octal input


Examples:

 ./IP-Manipulator.py 192.168.1.1

 ./IP-Manipulator.py 0xc0.0xa8.0x1.0x1

 ./IP-Manipulator.py 030052000401

 ./IP-Manipulator.py 192.168.1.1 -f output.txt