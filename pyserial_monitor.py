import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import serial
import time
import csv

def run():
    angle_data = []
    tentativas = 0
    num_max_tentativas = 10

    # Recebe a entrada e verifica se a porta de comunicacao serial e valida
    while True:
        try:
            serial_port = input("Insira a porta serial/usb do Arduino: ")
            serial_comm = serial.Serial(serial_port, 115200)
            tentativas = 0
            break
        except:
            print("Falha de comunicacao com a porta. Tente novamente.")
            tentativas += 1
            if tentativas > num_max_tentativas:
                print("Programa falhou em estabelecer contato com a porta de comunicacao serial.")
                return
            continue

    # Realiza chamadas para o Arduino ate conseguir receber o angulo do sensor
    while True:
        try:
            float(serial_comm.readline())
            break
        except ValueError:
            tentativas += 1
            if tentativas > num_max_tentativas:
                print("Erro ao receber dados do sensor.")
                return
            continue

    while True:
        try:
            run_time = input("Insira o tempo de amostra em segundos: ")
            break
        except ValueError:
            print("Valor invalido inserido.")
            continue

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

if __name__ == "__main__":
    run()
