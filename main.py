import serial
import bdd
import time

ser = serial.Serial('/dev/ttyUSB0', 115200)

#S1
t = 0
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
    global t, temperture, humidity, luminosity, pluvio_time, wind, pression, soil_temp, soil_humidity, girus, out_temp, out_humidity
    print('-'*50)
    print(f'Time: {t}sec')
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


def save_data():
    global temperture, humidity, luminosity, pluvio_time, wind, pression, soil_temp, soil_humidity, girus, out_temp, out_humidity
    bdd.insert_data_capteurs(temperture, out_temp, soil_temp, humidity, out_humidity, soil_humidity, pression, girus, wind, luminosity)

def treat_data(type:int):
    global t, temperture, humidity, luminosity, pluvio_time, wind, pression, soil_temp, soil_humidity, girus, out_temp, out_humidity
    try:
        if type == 1:
            t = float(t)
            temperture = float(temperture)
            humidity = float(humidity)
            luminosity = 1024-float(luminosity)

        elif type == 2:
            pluvio_time = float(pluvio_time)
            wind = float(wind)
            pression = float(pression)
            soil_temp = float(soil_temp)
        elif type == 3:
            soil_humidity = float(soil_humidity)
            girus = float(girus)
            out_temp = float(out_temp)
            out_humidity = float(out_humidity)
    except ValueError:
        return


last_save = time.time()
while True:
    if time.time() - last_save > 10:
        save_data()
        last_save = time.time()
    if ser.in_waiting > 0:
        data = ser.read_until(b'\n')
        try:
            data = data.decode('utf-8').strip()
            if len(data) and data[0] == 'S' and data[-1] == 'E':
                types_trame = int(data[1])
                if data[1] == '1':
                    data = data[3:-1].split(';')
                    t = data[0]
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
                treat_data(types_trame)
                display_data()
        except UnicodeDecodeError:
            pass
ser.close()