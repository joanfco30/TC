import RPi.GPIO as IO
import time

#configuro la board 
IO.setwarnings(False)
IO.setmode(IO.BOARD)

led = 40

IO.setup(led, IO.OUT)
IO.output(led, IO.LOW)

while True:
    i = 0
    while (i < 10):

        IO.output(led, IO.LOW)
        time.sleep(1)
        IO.output(led, IO.HIGH)
        time.sleep(1)
        print(f"El led de apaga y se enciende {i} veces")
        i = i+1
    IO.output(led, IO.LOW)
    exit()
