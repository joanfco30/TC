import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)


LED = 40
SW = 38
SW1 = 36

IO.setup(SW, IO.IN)
IO.setup(SW1, IO.IN)
IO.setup(LED, IO.OUT, initial= IO.LOW)

while True:
    if IO.input(SW1) == IO.HIGH:
        print(f"Saliendo del programa {IO.input(SW)}")
        exit()
    if IO.input(SW) == IO.HIGH:
        IO.output(LED, IO.LOW)
        time.sleep(0.5)
        IO.output(LED, IO.HIGH)
        time.sleep(0.5)
    print("Oprimir pulsador P1 para salir")
    print("Oprimir pulsador P2 para parpadear led")