# Sistema de Monitoração da Gaiola de Testes de Quadricópteros
Sistema de monitoração feito para a realização de testes de quadricopteros utilizando sensores.

## Arduino
A função do Arduino é se comunicar com o sensor magnético AS5040 e repassar os dados pela porta serial.
### Configuração dos Pinos
**Pino D2 -** Chip Selector


**Pino D3 -** Clock para sincronização de interface serial


**Pino D4 -** Recebe saída de dados do sensor


### Depedências
[Dash's AS5045 Library](https://github.com/DashZhang/AS5045)
### Datasheet do Sensor AS5040
[AS5040 10-bit Magnetic Rotary Encoder](https://ams.com/documents/20143/36005/AS5040_DS000374_3-00.pdf)

## Script Python
O script em Python recebe a saída serial do Arduino pela porta USB, aplica um filtro passa-baixa e retorna um gráfico para visualização dos resultados e exporta um csv para log e futuros processamentos de resultados.
### Utilização
O funcionamento do script é bem simples, basta informar a porta na qual o Arduino está conectado (a forma mais fácil de se descobrir essa informação é utilizando a Arduino IDE e indo em *Tools > Serial Port*) e o tempo em segundos para a coleta de dados.
### Depedências
+ Python3
+ python-tk
+ numpy
+ scipy
+ matplotlib
+ pyserial

## TODO
+ Melhorar filtragem
+ Mudar para comunicação sem fio utilizando o ESP-01
+ Avaliar 3 eixos de rotação
+ Desenvolver um servidor para comunicação com o ESP
+ Avaliação em tempo real
