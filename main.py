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
    global time, temperture, humidity, luminosity, pluvio_time, wind, pression, soil_temp, soil_humidity, girus, out_temp, out_humidity
    print('-'*50)
    print(f'Time: {time}sec')
    print(f'Temperture: {temperture}°C')
    print(f'Humidity: {humidity}%')
    print(f'Luminosity: {luminosity}')
    print(f'Pluvio Time: {pluvio_time}sec')
    print(f'Wind: {wind}')
    print(f'Pression: {pression}')
    print(f'Soil Temp: {soil_temp}')
    print(f'Soil Humidity: {soil_humidity}')
    print(f'Girus: {girus}')
    print(f'Out Temp: {out_temp}')
    print(f'Out Humidity: {out_humidity}')


def treat_data():
    global time, temperture, humidity, luminosity, pluvio_time, wind, pression, soil_temp, soil_humidity, girus, out_temp, out_humidity
    try:
        time = float(time)
        temperture = float(temperture)
        humidity = float(humidity)
        luminosity = float(luminosity)

        pluvio_time = float(pluvio_time)
        wind = float(wind)
        pression = float(pression)
        soil_temp = float(soil_temp)

        soil_humidity = float(soil_humidity)
        girus = float(girus)
        out_temp = float(out_temp)
        out_humidity = float(out_humidity)
    except ValueError:
        return


while True:
    if ser.in_waiting > 0:
        data = ser.read_until(b'\n')
        try:
            data = data.decode('utf-8').strip()
            if len(data) and data[0] == 'S' and data[-1] == 'E':
                if data[1] == '1':
                    data = data[3:-1].split(';')
                    time = data[0]
                    temperture = data[1]
                    humidity = data[2]
                    luminosity = data[3]
                elif data[1] == '2':
                    data = data[3:-1].split(';')
                    pluvio_time = data[0]
                    wind = data[1]
                    pression = data[2]
                    soil_temp = data[3]
                elif data[1] == '3':
                    data = data[3:-1].split(';')
                    soil_humidity = data[0]
                    girus = data[1]
                    out_temp = data[2]
                    out_humidity = data[3]
                treat_data()
                display_data()
        except UnicodeDecodeError:
            pass
ser.close()