#!/usr/bin/python

import paho.mqtt.client as paho
import os
import socket
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    client.subscribe("#" , 1 )

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "a1bgnbjjx7840d.iot.us-west-2.amazonaws.com"
awsport = 8883
clientId = "sameers_pi"
thingName = "sameers_pi"
caPath = "/home/pi/deviceSDK/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem"
certPath = "/home/pi/deviceSDK/728abdac8d-certificate.pem.crt"
keyPath = "/home/pi/deviceSDK/728abdac8d-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_forever()

