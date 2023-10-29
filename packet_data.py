import serial
import csv
import os

ser = serial.Serial('COM6', 9600)

csv_filename = 'receivedPackets.csv'

file = open(csv_filename, 'a')
print("file created")

while True:
    getData = str(ser.readline().decode('utf-8').strip())
    print(getData)
    file.write(getData + "\n")
    file.flush()
