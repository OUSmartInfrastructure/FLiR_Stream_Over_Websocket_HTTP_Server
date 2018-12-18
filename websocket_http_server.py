import socket
import os
import re
from PIL import Image
import scipy.misc
from websocket_server import WebsocketServer
import time
import threading
import ConfigParser
import base64
import sys
import cv2
import cv
import numpy as np
import matplotlib.pyplot as plt
from pylepton import Lepton

def program_start():
	parser = ConfigParser.RawConfigParser()
	configFilePath =r'server.conf'
	parser.read(configFilePath)
	http_interface = parser.get('Server-Configurations', 'HTTP_Interface')
	http_port = parser.get('Server-Configurations', 'HTTP_Port')
	http_listen = parser.get('Server-Configurations', 'HTTP_Listen')
	http_listen = int(http_listen)
	http_recieve = parser.get('Server-Configurations', 'HTTP_Recieve')
	http_recieve = int(http_recieve)
	websocket_interface = parser.get('Server-Configurations', 'Websocket_Interface')
	websocket_port = parser.get('Server-Configurations', 'Websocket_Port')
	websocket_port = int(websocket_port)
	image_path = parser.get('Server-Configurations', 'Image')
	def capture(device = "/dev/spidev0.0"):
		with Lepton(device) as l:
			a,_ = l.capture()
		cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
		np.right_shift(a, 8, a)
		return np.uint8(a)

	def save_image():
		while True:
			image = capture()
			im = plt.imsave("thermal.jpg",np.fliplr(image.mean(2)),cmap="jet")
	def http_server():
		addr = socket.getaddrinfo(http_interface, http_port)[0][-1]
		s = socket.socket()
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind(addr)
		s.listen(http_listen)
		print('listening on', addr)
		while True:
			c1, addr = s.accept()
	        	print repr(c1.recv(http_recieve))
	        	print('client connected from',addr)
			data = open("index.html", 'rb')
			data = data.read()
	        	c1.send(data)
			time.sleep(.01)
	       		c1.close()
			
        def setIP():
                while True:
                        ip = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
                        print(ip)
                        html_code = []
                        html = open("index.html","r")
                        for line in html:
                                html_code.append(line)
                        for line in html_code:
                                match = re.findall('var s = new WebSocket',line)
                                if len(match)>0:
                                        position=html_code.index(line)
                        html_code[9] = '        var s = new WebSocket("ws://%s:9876/");\n' %ip
                        with open("index.html","w") as index:
                                for line in html_code:
                                        index.write(str(line))
                        time.sleep(60)



	def websocket_server():
		global i
		i=0
		def new_client(client, server):
			global i
			i=((i+1))
			def start_data_stream():
				data_limit = 2000
				while True:
					check = os.stat('thermal.jpg')
					#Add a wait in, due to file access speed
					time.sleep(.005)
					try:
						if check>=data_limit:
							with open(image_path, "rb") as image_file:
								thermal=base64.b64encode(image_file.read())
							server.send_message_to_all(thermal)
						else:
							pass
					except:
						pass
			if i == 1:
				threading.Thread(target=start_data_stream).start()
			else:
				pass

		        print("New client connected and was given id %d" % client['id'])

		def client_left(client, server):
		        print("Client(%d) disconnected" % client['id'])

		PORT=9876
		server = WebsocketServer(websocket_port,host=websocket_interface)
		server.set_fn_new_client(new_client)
		server.set_fn_client_left(client_left)
		server.run_forever()

	threading.Thread(target=save_image).start()
	threading.Thread(taget=setIP).start
	threading.Thread(target=websocket_server).start()
	threading.Thread(target=http_server).start()
program_start()
