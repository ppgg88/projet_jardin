import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    if ser.in_waiting > 0:
        print(ser.readline().decode('utf-8').strip())

ser.close()
