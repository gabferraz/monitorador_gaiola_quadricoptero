import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import serial
import time
import csv

angle_data = []
while True:
    try:
        serial_port = raw_input("Insira a porta serial/usb do Arduino: ")
        serial_comm = serial.Serial(serial_port, 115200)
        break
    except:
        print("Falha de comunicacao com a porta. Tente novamente.")
        continue

while True:
    try:
        float(serial_comm.readline())
        break
    except ValueError:
        continue
run_time = input("Insira o tempo de amostra em segundos: ")
print("Iniciando amostragem.")

start_time = time.time()
while((time.time() - start_time) < run_time):
    angle_data.append(float(serial_comm.readline()))

b, a = butter(3, 0.06)
filtered_data = filtfilt(b, a, angle_data)
plt.plot(filtered_data)
plt.ylabel("Deslocamento Angular")
plt.show()

wtr = csv.writer(open('output.csv', 'w'), delimiter=',', lineterminator='\n')
for x in filtered_data: wtr.writerow([x])
