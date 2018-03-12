global_rssi = 0

import os, sys, time, struct
import bluetooth._bluetooth as bluez
import bluetooth
import threading
from time import gmtime, strftime

from PyQt4 import QtCore, QtGui
sys.path.insert(0, 'User_Interface/')
sys.path.insert(0, 'Bluetooth/')
sys.path.insert(0, 'Sensors/')
sys.path.insert(0, 'Comms/')

from output import Ui_MainDisplayWindow
from inquiry_rssi import *

from test_discovery import *
from serial_test import *
from mqtt_test import *

#import the ZMQ libraries
import zmq

import boto3
from aws_conf import *

import global_types

class zmqClient(object):
    def __init__(self):
	self.port_num = "9001"

    def RunZMQClient(self):
	context = zmq.Context()
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://192.168.141.172:%s" % self.port_num)
	socket.send("milk")
	message = socket.recv()
	print(message)
'''
class BluetoothThread(object):
	def __init__(self):
		thread = threading.Thread(target=self.Bluetooth_Beaconing, args = ())
		thread.daemon = True
		thread.start()

	def Bluetooth_Beaconing(self):
		dev_id = bluez.hci_get_route("B8:27:EB:EF:CB:3D")
		try:
			sock = bluez.hci_open_dev(dev_id)
		except:
			print("error accessing bluetooth device...")
			sys.exit(1)

		try:
			mode = read_inquiry_mode(sock)
		except Exception as e:
			print("error reading inquiry mode.  ")
			print("Are you sure this a bluetooth 1.2 device?")
			print(e)
			sys.exit(1)
		print("current inquiry mode is %d" % mode)

		if mode != 1:
			print("writing inquiry mode...")
			try:
				result = write_inquiry_mode(sock, 1)
			except Exception as e:
				print("error writing inquiry mode.  Are you sure you're root?")
				print(e)
				sys.exit(1)
			if result != 0:
				print("error while setting inquiry mode")
			print("result: %d" % result)
	
		while True:
			device_inquiry_with_with_rssi(sock)
'''
class BluetoothThread(object):
	def __init__(self):
            
            thread = threading.Thread(target=self.Bluetooth_Beaconing, args = ())
	    thread.daemon = True
	    thread.start()

	def Bluetooth_Beaconing(self):
            while True:
		start_ble_beaconing()

class CheckObjectPresence(object):
    def __init__(self):
        #Add any initialization logic here
	mqtt_init()
        print("Starting the thread!")
        thread = threading.Thread(target=self.PushDataToAWS, args = ())
        thread.daemon = True
        thread.start()

    def PushDataToAWS(self):
        print("Checking for the MAC")
        #Check for MAC: 48:3B:38:BD:A3:9C
        while True:
        #    if(global_types.gl_ble_address == "48:3B:38:BD:A3:9C"):
		while (float(global_types.gl_adc_sensor_val) > 100):
			pass
		global_types.gl_numItem += 1
		send_msg = {"ItemID": "12345","Time": strftime("%H:%M:%S",gmtime()),"ItemCount":global_types.gl_numItem}
		global_types.mqttc.publish("data", json.dumps(send_msg), qos=0)
                #socket.send("milk")
		print(global_types.gl_ble_address, global_types.gl_ble_rssi_val, global_types.gl_adc_sensor_val)
                global_types.gl_ble_address = None
		sleep(2)

class ML_Model(object):
    #def __init__(self):
    #    thread = threading.Thread(target=self.Create_Endpoint, args = ())
    #    thread.daemon = True
    #    thread.start()

    #Static variables that can be used across all class functions
    end_point_url = None

    def CreateEndpoint(self, client):
        # Create a Real-Time Endpoint in order to enable predictions.
        response_dict_create = client.create_realtime_endpoint(
                MLModelId = MILK_ML_IDENTIFIER
        )
        # Store the URL for the ML model
        self.end_point_url = response_dict_create.get('RealtimeEndpointInfo').get('EndpointUrl')
        #print(self.end_point_url)
        '''
        for x in response_dict_create:
            print(x, response_dict_create[x])
            print("\n")
        '''

    def DescribeMLModel(self, client):
        #Get the description of the ML model from AWS
        response_ML_description = client.describe_ml_models()
        self.end_point_url = response_ML_description.get('Results')[2].get('EndpointInfo').get('EndpointUrl')

    def DeleteEndpoint(self, client):
        #Delete the Real-Time Endpoint once you are done with the predictions
        response_dict_delete = client.delete_realtime_endpoint(
                MLModelId = MILK_ML_IDENTIFIER
        )
        #print("Delete Instance output dict:")
        #print(response_dict_delete)
        '''
        for x in response_dict_delete:
            print(x, response_dict_delete[x])
            print("\n")
        '''

    def PredictOutcome(self, client, item_1, item_2):
        prediction_outcome = client.predict (
                MLModelId = MILK_ML_IDENTIFIER,
                Record = {
                    'item1' : item_1,
                    'item2' : item_2
                },
                PredictEndpoint = str(self.end_point_url)
            )
        #print(prediction_outcome)
        #print(prediction_outcome.get('Prediction').get('predictedScores').get('1'))
        return (prediction_outcome.get('Prediction').get('predictedScores').get('1'))

if __name__ == '__main__':
   
    #Initialize global types
    global_types.init()

    #Start the Bluetooth Beaconing as a thread
    example = BluetoothThread()
    
    # Start the serial input from the Arduino ADC
    signal.signal(signal.SIGINT, signal_handler)
    test = fsrThread()
    
    check_fsr_val = CheckObjectPresence()

    #Start the zmq socket
    client = zmqClient()
    client.RunZMQClient()

    '''
    # This is the machine learning API call
    instance_1 = boto3.client('machinelearning',\
                        region_name=SERVICE_REGION,\
                        aws_access_key_id=AWS_ACCESS_ID,
                        aws_secret_access_key=AWS_ACCESS_KEY)

    model_ML = ML_Model()
    model_ML.DescribeMLModel(instance_1)
    prediction_value = model_ML.PredictOutcome(instance_1, 'rice', 'nachos')
    print(prediction_value)
    '''
    while(1 == 1):
        pass
