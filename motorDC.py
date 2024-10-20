"""Control motor DC con raspberry Pi"""

import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)

right = 8
left = 10

IO.setup(right, IO.OUT, initial = IO.LOW)
IO.setup(left, IO.OUT, initial = IO.LOW)

while True:
    valor = input("""Ingrese 'r' - 'i' para activar el motor y's' para detener: """)
    if valor == 'r':
        IO.output(right, IO.HIGH)
        IO.output(left, IO.LOW)
        time.sleep(0.2)
    if valor == 'l':
        IO.output(right, IO.LOW)
        IO.output(left, IO.HIGH)
        time.sleep(0.2)
    if valor == 's':
        IO.output(right, IO.LOW)
        IO.output(left, IO.LOW)
        time.sleep(0.2)
    x = input("Escriba 'x' y enter para salir: ")
    if x == 'x':
        IO.output(right, IO.LOW)
        IO.output(left, IO.LOW)
        exit()

