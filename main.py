import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    if ser.in_waiting > 0:
        print(ser.readline())

ser.close()
