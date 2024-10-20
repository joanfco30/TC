"""Programa para controlar las salidad PWM
    (Pulse Width Modulation)"""

import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BOARD)

RED = 3
GREEN = 5
BLUE = 7
IO.setup(RED, IO.OUT, initial=IO.LOW)
IO.setup(GREEN, IO.OUT, initial= IO.LOW)
IO.setup(BLUE, IO.OUT, initial= IO.LOW)

while True:
    for i in range(4):
        IO.output(RED, IO.HIGH)
        IO.output(GREEN,IO.LOW)
        IO.output(BLUE, IO.LOW)
        time.sleep(2)
        IO.output(RED, IO.LOW)
        IO.output(GREEN,IO.HIGH)
        IO.output(BLUE, IO.LOW)
        time.sleep(2)
        IO.output(RED, IO.LOW)
        IO.output(GREEN,IO.LOW)
        IO.output(BLUE, IO.HIGH)
        time.sleep(2)
    IO.output(RED, IO.LOW)
    IO.output(GREEN,IO.LOW)
    IO.output(BLUE, IO.LOW)
    time.sleep(2)
    exit()
