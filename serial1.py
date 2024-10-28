import serial

ser = serial.Serial("/dev/ttyS0",baudrate = 9500)


while True:
    print(ser.read_until(b'\n').decode())
    #print(ser.read(size = 3).decode())
    val = "Valor recibido"
    ser.write(val.encode())