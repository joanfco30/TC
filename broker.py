import random
import time
import paho.mqtt.client as mqtt
# Configuraci ?on del broker y temas MQTT
broker_address = "192.168.100.41" # Direcci ?on IP del broker MQTT
Temperatura = "Temperatura" # T ?opico para enviar la temperatura
Humedad = "Humedad" # T ?opico para enviar la humedad
Led = "Led" # T ?opico para recibir mensajes relacionados con el LED
Slider = "Slider" # T ?opico para recibir mensajes de un slider
# Crear el cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2) # Crear instancia del cliente MQTT
# Funci ?on de callback para manejar mensajes recibidos en los t ?opicos suscritos
 
def on_message(client, userdata, message):
    # Decodificar el mensaje recibido y mostrarlo
    recibido = message.payload.decode()
    print(f"Mensaje recibido en el t ?opico ?{message.topic}?: {recibido}")
    # Asignar la funci ?on de callback al cliente MQTT para manejar mensajes entrantes
client.on_message = on_message
# Conectar al broker MQTT
client.connect(broker_address)
# Funci ?on para publicar datos de temperatura y humedad
 
def publicar():
    while True:
        # Generar un valor aleatorio de temperatura entre 1.0 y 100.0
        temperatura = round(random.uniform(1.0, 100.0), 2)
        client.publish(Temperatura, temperatura) # Publicar en el t ?opico de temperatura
        print(f"Publicado: Temperatura={temperatura:.2f}°C")
        # Generar un valor aleatorio de humedad entre 1.0 y 100.0
        humedad = round(random.uniform(1.0, 100.0), 2)
        client.publish(Humedad, humedad) # Publicar en el t ?opico de humedad
        print(f"Publicado: Humedad={humedad:.2f}%")
        # Esperar 3 segundos antes de enviar los siguientes datos
        time.sleep(3)
        # Funcion para suscribirse a un t ?opico y recibir mensajes en tiempo real
 
def suscribir():
    client.subscribe(Led) # Suscribirse al t ?opico del LED para recibir mensajes
    client.subscribe(Slider) # Suscribirse al t ?opico del Slider para recibir mensajes
    client.loop_start() # Iniciar el loop del cliente para recibir mensajes
    # Bloque principal del programa
try:
    suscribir() # Iniciar suscripci ?on al t ?opico para recibir comandos
    publicar() # Iniciar publicaci ?on de datos de temperatura y humedad
except KeyboardInterrupt:
    print("Programa detenido por el usuario")
finally:
    client.loop_stop() # Detener el loop del cliente
    client.disconnect() # Desconectar del broker MQTT
    print("Cliente MQTT desconectado")
