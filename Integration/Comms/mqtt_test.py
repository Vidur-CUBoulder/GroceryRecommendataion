#!/usr/bin/env python
import paho.mqtt.client as p
import os
import socket
import ssl
import sys
import json
from time import sleep
from random import uniform

import global_types
sys.path.insert(0, '../Integration/')

connflag = False

def on_connect(client, userdata, flags, rc):
	global connflag
	connflag = True
	print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

def mqtt_init():
	global_types.mqttc = p.Client()
	global_types.mqttc.on_connect = on_connect
	global_types.mqttc.on_message = on_message
	awshost = "a1bgnbjjx7840d.iot.us-west-2.amazonaws.com"
	awsport = 8883
	clientId = "sameers_pi"
	thingName = "sameers_pi"
	caPath = "./Comms/temp/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem"
	certPath = "./Comms/temp/728abdac8d-certificate.pem.crt"
	keyPath = "./Comms/temp/728abdac8d-private.pem.key"
	global_types.mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
	global_types.mqttc.connect(awshost, awsport, keepalive=60)
	global_types.mqttc.loop_start()

#	while 1==1:
#		sleep(0.5)
#		if connflag == True:
#			print(temp)
#			send_msg = {"ItemID": "12345","Time": "1:25"}
#			mqttc.publish("data", json.dumps(send_msg), qos=0)
#			temp += 1
#		        mqttc.publish("data", tempreading, qos=1)
#		        print("msg sent: temperature " + "%d" % tempreading )
#		else:
#			print("waiting for connection...")
