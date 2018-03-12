#!/usr/bin/env python
import signal
import sys
import serial
import threading

def signal_handler(signal, frame):
	print("Ctrl + C captured, exitting.")
	sys.exit(0)

class fsrThread(object):
	def __init__(self):
		thread = threading.Thread(target=self.read_thread, args = ())
		thread.daemon = True
		thread.start()

	def open_serial(self):
		#open a serial port
		self.ser = serial.Serial('/dev/ttyACM0')
		print("Port opened:" + self.ser.name)

	def read_thread(self):
		self.open_serial()
		while True:
			x = self.ser.readline()
			#y = float(str(x).split("'")[1].split("\\r")[0])
			#if y > 0:
			print(str(x))

if __name__ == '__main__':
	signal.signal(signal.SIGINT, signal_handler)
	test = fsrThread()
	while True:
		pass

