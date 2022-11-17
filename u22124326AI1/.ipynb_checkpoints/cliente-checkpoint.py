import threading
import sys
import socket
import pickle
import os

class Cliente():

	def __init__(self, host=input("Intoduzca la IP del servidor ?  "), port=int(input("Intoduzca el PUERTO del servidor ?  "))):
		self.s = socket.socket()
		self.s.connect((host, int(port)))
		print('\n\tProceso con PID = ',os.getpid(), '\n\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\n\tTotal Hilos activos en este punto del programa =', threading.active_count())
		threading.Thread(target=self.recibir, daemon=True).start()

		nick = input("Ingresa tu nickname:")
		while True:
			msg = input('\nEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1 \n')
			if msg == '1':
				print(" **** Me piro vampiro; cierro socket y mato al CLIENTE con PID = ", os.getpid())
				self.s.close()
				sys.exit()
			else:
				with open("22124326.txt", "a") as f:
					msg = input("Escriba el mensaje:")
					f.write("\n" + nick + " - " + msg)
					self.enviar(msg)
				

	def recibir(self):
		print('\nHilo RECIBIR con ID =',threading.currentThread().getName(), '\n\tPertenece al PROCESO con PID', os.getpid(), "\n\tHilos activos TOTALES ", threading.active_count())
		while True:
			try:
				data = self.s.recv(32)
				if data: print(pickle.loads(data))
			except: pass

	def enviar(self, msg):
		self.s.send(pickle.dumps(msg))

arrancar = Cliente()

		