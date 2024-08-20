import sqlite3
import time

conn = sqlite3.connect('base_jardin.db')

# create table
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS `capteurs` (
    `id` int NOT NULL,
    `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `Tserre` float NOT NULL,
    `Text` float NOT NULL,
    `Tsol` float NOT NULL,
    `Hserre` float NOT NULL,
    `Hext` float NOT NULL,
    `Hsol` float NOT NULL,
    `P` float NOT NULL,
    `girus` float NOT NULL,
    `windspeed` float NOT NULL,
    `luminosity` int NOT NULL,
    PRIMARY KEY (`id`)
    )''')

conn.commit()


cursor.execute('''CREATE TABLE IF NOT EXISTS `pluvio` (
    `id` int NOT NULL,
    `time` timestamp NOT NULL,
    PRIMARY KEY (`id`)
    )''')

conn.commit()


def insert_data_capteurs(Tserre, Text, Tsol, Hserre, Hext, Hsol, P, girus, windspeed, luminosity):
    #get max id : 
    cursor.execute('''SELECT MAX(id) FROM capteurs''')
    max_id = cursor.fetchone()[0]
    if max_id is None:
        max_id = -1

    cursor.execute('''INSERT INTO capteurs (id, time, Tserre, Text, Tsol, Hserre, Hext, Hsol, P, girus, windspeed, luminosity) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (max_id+1, int(time.time()), Tserre, Text, Tsol, Hserre, Hext, Hsol, P, girus, windspeed, luminosity))
    conn.commit()



