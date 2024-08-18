import serial

ser = serial.Serial('COM7', 115200)

while True:
    if ser.in_waiting > 0:
        data = ser.read_until(b'\n')
        try:
            data = data.decode('utf-8').strip()
            if len(data) and data[0] == 'S' and data[-1] == 'E':
                print(data)
        except UnicodeDecodeError:
            pass
ser.close()
