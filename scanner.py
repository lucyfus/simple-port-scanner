import socket

#Pide la IP del host
host = input("Ingresa la IP del host a escanear: ")

#Pide rango de puertos
puerto_inicio = int(input("Puerto inicial: "))
puerto_final = int(input("Puerto final: "))

puertos_abiertos = []

print(f"Escaneando {host} desde el puerto {puerto_inicio} hasta {puerto_final}...")

for puerto in range(puerto_inicio, puerto_final + 1):
	#Crea un socket TCP/IPv4
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1.0) #Espera 1 segundo por respuesta
	try:
	#Intenta conectar
		resultado = s.connect_ex((host, puerto)) #Devuelve 0 si está abierto
		if resultado == 0:
			puertos_abiertos.append(puerto)
			print(f"puerto {puerto} abierto")
	finally:
		s.close()

if puertos_abiertos:
	print("Puertos abiertos entontrados: ")
	for p in puertos_abiertos:
		print(f"- Puerto {p}")
else:
	print("No se encontraron puertos abiertos.")


import datetime

with open("puertos_abiertos.txt", "a") as archivo:
	archivo.write("\n--- Escaneo ---\n")
	archivo.write(f"Host: {host}\n")
	archivo.write(f"Fecha: {datetime.datetime.now()}\n")
	if puertos_abiertos:
		archivo.write("Puertos abiertos:\n")
		for p in puertos_abiertos:
			archivo.write(f"- Puerto {p}\n")
	else:
		archivo.write("No se encontraron puertos abiertos.\n")


print("Escaneo finalizado.")
