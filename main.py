import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

#S1
time = 0
temperture = 0
humidity = 0
luminosity = 0

#S2
pluvio_time = 0
wind = 0
pression = 0
soil_temp = 0

#S3
soil_humidity = 0
girus = 0
out_temp = 0
out_humidity = 0

def display_data():
    print(f'S1: Time: {time} Temperture: {temperture} Humidity: {humidity} Luminosity: {luminosity}')
    print(f'S2: Time: {pluvio_time} Wind: {wind} Pression: {pression} Soil Temp: {soil_temp}')
    print(f'S3: Soil Humidity: {soil_humidity} Girus: {girus} Out Temp: {out_temp} Out Humidity: {out_humidity}')

while True:
    if ser.in_waiting > 0:
        data = ser.read_until(b'\n')
        try:
            data = data.decode('utf-8').strip()
            if len(data) and data[0] == 'S' and data[-1] == 'E':
                if data[1] == '1':
                    data = data[2:-1].split(';')
                    time = data[0]
                    temperture = data[1]
                    humidity = data[2]
                    luminosity = data[3]
                elif data[1] == '2':
                    data = data[2:-1].split(';')
                    pluvio_time = data[0]
                    wind = data[1]
                    pression = data[2]
                    soil_temp = data[3]
                elif data[1] == '3':
                    data = data[2:-1].split(';')
                    soil_humidity = data[0]
                    girus = data[1]
                    out_temp = data[2]
                    out_humidity = data[3]
                display_data()
        except UnicodeDecodeError:
            pass
ser.close()