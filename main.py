import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid)
        
```
This will list all the available serial ports on your system. You can run this script to see if the port is available or not.
If you are using a Linux system, you can use the `ls /dev/tty*` command to list all the available serial ports.
If you are using a Windows system, you can use the Device Manager to check the available serial ports.
Once you have identified the correct port, you can update your Python script to use that port.
```
