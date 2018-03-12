global_rssi = 0

import os, sys, time, struct
import bluetooth._bluetooth as bluez
import bluetooth
import threading
from time import gmtime, strftime

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

sys.path.insert(0, 'User_Interface/')
sys.path.insert(0, 'Bluetooth/')
sys.path.insert(0, 'Sensors/')
sys.path.insert(0, 'Comms/')
sys.path.insert(0, 'TTS/')

from test_discovery import * 

#from output import Ui_MainDisplayWindow
from inquiry_rssi import *

from test_discovery import *
from serial_test import *
from mqtt_test import *

#Import the ML/AWS libraries
import boto3
from aws_conf import *

#import Global variables
import global_types

#import the ZMQ libraries
import zmq

#import the user interface files
#from user_interface import Ui_Recommend_Dialog 
from final_user_interface import * 
#from Login import Ui_Login_Dialog 

#import the TTS functionality
from gtts_test import *

global message
message = ""

def signal_handler(signal, frame):
	print("Ctrl + C captured, exitting.")
	sys.exit(0)

class zmqServer(object):
	def __init__(self):
		self.port_num = "9001" 
 		thread = threading.Thread(target=self.RunZMQServer, args = ())
		thread.daemon = True
		thread.start()

	def RunZMQServer(self):
		while True:
			context = zmq.Context()
			socket = context.socket(zmq.REP)
			socket.bind("tcp://*:%s" % self.port_num)
			message = socket.recv()
			print("Receive request: ", message) 
			sleep(1)
			global_types.checkBox_set_3_1 = str(message)
			#socket.send("World from %s" % self.port_num)

class BluetoothThread(object):
	def __init__(self):
		thread = threading.Thread(target=self.Bluetooth_Beaconing, args = ())
		thread.daemon = True
		thread.start()

	def Bluetooth_Beaconing(self):
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
			print(global_types.gl_ble_address, global_types.gl_ble_rssi_val, global_types.gl_adc_sensor_val)
			global_types.gl_ble_address = None
			sleep(2)

class ML_Model(object):
    #def __init__(self):
    #    thread = threading.Thread(target=self.Create_Endpoint, args = ())
    #    thread.daemon = True
    #    thread.start()

    #Static variables that can be used across all class functions
    global_types.end_point_url = None

    def CreateEndpoint(self, client, item_identifier):
        # Create a Real-Time Endpoint in order to enable predictions.
        response_dict_create = client.create_realtime_endpoint(
                MLModelId = item_identifier
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
        global_types.end_point_url = response_ML_description.get('Results')[2].get('EndpointInfo').get('EndpointUrl')

    def DeleteEndpoint(self, client, item_identifier):
        #Delete the Real-Time Endpoint once you are done with the predictions
        response_dict_delete = client.delete_realtime_endpoint(
                MLModelId = item_identifier
        )
        #print("Delete Instance output dict:")
        #print(response_dict_delete)
        '''
        for x in response_dict_delete:
            print(x, response_dict_delete[x])
            print("\n")
        '''

    def PredictOutcome(self, item_identifier, client, item_1, item_2):
		prediction_outcome = client.predict (
                MLModelId = item_identifier,
                Record = {
                    'item1' : item_1,
                    'item2' : item_2
                },
                PredictEndpoint = str(global_types.end_point_url)
            )
        #print(prediction_outcome)
        #print(prediction_outcome.get('Prediction').get('predictedScores').get('1'))
		return (prediction_outcome.get('Prediction').get('predictedScores').get('1'))

class LoginGUIApplication(QtGui.QMainWindow):
	def __init__(self):
		super(LoginGUIApplication, self).__init__()

		self.ui_login = Ui_Login_Dialog()
		self.ui_login.setupUi(self)

		self.ui_login.pushButton.clicked.connect(self.push_func)	

	def push_func(self, check_toggle):
		print("In pushbutton! ", check_toggle)
		print(self.ui_login.textEdit.toPlainText())
		print(self.ui_login.textEdit_2.toPlainText())
		
		if(str(self.ui_login.textEdit.toPlainText()) == "vidur" and
			str(self.ui_login.textEdit_2.toPlainText()) == "eid"):
			pass
			#global_types.stupid_ret_val = True	
			#gui_login.quit()
			#sys.exit(gui_login.exec_())
		else:
			#Show something!??
			print("Auth Failed!")
		

class GUIApplication(QtGui.QMainWindow):
	def __init__(self):
		super(GUIApplication, self).__init__()

		#self.ui = Ui_MainDisplayWindow()
		self.ui = Ui_Recommend_Dialog()
		self.ui.setupUi(self)
	
		#Check Boxes
		self.ui.checkBox_1.toggled.connect(self.checkBox_1)
		self.ui.checkBox_2.toggled.connect(self.checkBox_2)
		self.ui.checkBox_3.toggled.connect(self.checkBox_3)
		self.ui.checkBox_4.toggled.connect(self.checkBox_4)
		self.ui.checkBox_5.toggled.connect(self.checkBox_5)
		self.ui.checkBox_6.toggled.connect(self.checkBox_6)

		#Push Buttons
		self.ui.pushButton.clicked.connect(self.active_suggest)		

	def active_suggest(self, check_toggle):
		suggest = "Milk"
		Max = global_types.avg_milk_ML_val
		if(global_types.avg_beer_ML_val > Max):
			Max = global_types.avg_beer_ML_val
			suggest = "Beer"
		if(global_types.avg_soap_ML_val > Max):
			Max = global_types.avg_soap_ML_val
			suggest = "Soap"

		print(check_toggle)
		print(global_types.avg_milk_ML_val, global_types.avg_beer_ML_val, global_types.avg_soap_ML_val)
		print(suggest)
		
		#self.ui.label_4.setText("Milk")
		#self.ui.label_8.setText("Beer")
		#self.ui.label_6.setText("Soap")
		
		self.ui.label_5.setText(str(global_types.avg_milk_ML_val))
		self.ui.label_7.setText(str(global_types.avg_beer_ML_val))
		self.ui.label_9.setText(str(global_types.avg_soap_ML_val))	

		#Say my name, !xobile !! 
		appended_string = "The recommender suggests that you might like to buy " + suggest
		text_op(str(appended_string))		

	def checkBox_1(self, checked):
		#print("checkBox_1: ", checked)
		if(checked == True):
			global_types.checkBox_set_1_0 = self.ui.textEdit_1.toPlainText() 
			print(global_types.checkBox_set_1_0)
		else:
			global_types.checkBox_set_1_0 = None
	
	def checkBox_2(self, checked):
		#print("checkBox_2: ", checked)
		if(checked == True):
			global_types.checkBox_set_1_1 = self.ui.textEdit_2.toPlainText()
			print(global_types.checkBox_set_1_1)	
		else:
			global_types.checkBox_set_1_1 = None	


	def checkBox_3(self, checked):
		#print("checkBox_3: ", checked)
		if(checked == True):
			global_types.checkBox_set_2_0 = self.ui.textEdit_3.toPlainText()
			print(global_types.checkBox_set_2_0)
		else:
			global_types.checkBox_set_2_0 = None

	def checkBox_4(self, checked):
		#print("checkBox_4: ", checked)	
		if(checked == True):
			global_types.checkBox_set_2_1 = self.ui.textEdit_4.toPlainText()
			print(global_types.checkBox_set_2_1)
		else:
			global_types.checkBox_set_2_1 = None

	def checkBox_5(self, checked):
		#print("checkBox_5: ", checked)	
		if(checked == True):
			global_types.checkBox_set_3_0 = self.ui.textEdit_5.toPlainText()
			print(global_types.checkBox_set_3_0)
		else:
			global_types.checkBox_set_3_0 = None
	
	def checkBox_6(self, checked):
		#print("checkBox_6: ", checked)	
		if(checked == True):
			global_types.checkBox_set_3_1 = self.ui.textEdit_6.toPlainText()
			print(global_types.checkBox_set_3_1)
		else:
			global_types.checkBox_set_3_1 = None


class PredictionThread_Set1(object):
	def __init__(self, instance_milk, instance_beer, instance_soap):
		thread = threading.Thread(target=self.StartThread, args = ())
		thread.daemon = True
		thread.start()

	def StartThread(self):
		while True:
			while(global_types.checkBox_set_1_0 == None or global_types.checkBox_set_1_1 == None):
				sleep(1)
				continue
					
			global_types.milk_ML_val_Set1 = ML_Model().PredictOutcome(MILK_ML_IDENTIFIER, instance_milk,\
							str(global_types.checkBox_set_1_0),\
							str(global_types.checkBox_set_1_1))
			if(global_types.milk_ML_val_Set1 == None):
				global_types.milk_ML_val_Set1 = 0
			
			global_types.beer_ML_val_Set1 = ML_Model().PredictOutcome(BEER_ML_IDENTIFIER, instance_beer,\
							str(global_types.checkBox_set_1_0),\
							str(global_types.checkBox_set_1_1))
			if(global_types.beer_ML_val_Set1 == None):
				global_types.beer_ML_val_Set1 = 0	
			
			global_types.soap_ML_val_Set1 = ML_Model().PredictOutcome(SOAP_ML_IDENTIFIER, instance_soap,\
							str(global_types.checkBox_set_1_0),\
							str(global_types.checkBox_set_1_1))
			if(global_types.soap_ML_val_Set1 == None):
				global_types.soap_ML_val_Set1 = 0	
			
			global_types.checkBox_set_1_0 = None
			global_types.checkBox_set_1_1 = None
			
			global_types.avg_milk_ML_val = (global_types.milk_ML_val_Set1 + global_types.milk_ML_val_Set2 + global_types.milk_ML_val_Set3)/3
			global_types.avg_beer_ML_val = (global_types.beer_ML_val_Set1 + global_types.beer_ML_val_Set2 + global_types.beer_ML_val_Set3)/3
			global_types.avg_soap_ML_val = (global_types.soap_ML_val_Set1 + global_types.soap_ML_val_Set2 + global_types.soap_ML_val_Set3)/3


class PredictionThread_Set2(object):
	def __init__(self, instance_milk, instance_beer, instance_soap):
		thread = threading.Thread(target=self.StartThread, args = ())
		thread.daemon = True
		thread.start()

	def StartThread(self):
		while True:
			while(global_types.checkBox_set_2_0 == None or global_types.checkBox_set_2_1 == None):
				sleep(1)
				continue
					
			global_types.milk_ML_val_Set2 = ML_Model().PredictOutcome(MILK_ML_IDENTIFIER, instance_milk,\
							str(global_types.checkBox_set_2_0),\
							str(global_types.checkBox_set_2_1))
			if(global_types.milk_ML_val_Set2 == None):
				global_types.milk_ML_val_Set2 = 0
			
			global_types.beer_ML_val_Set2 = ML_Model().PredictOutcome(BEER_ML_IDENTIFIER, instance_beer,\
							str(global_types.checkBox_set_2_0),\
							str(global_types.checkBox_set_2_1))
			if(global_types.beer_ML_val_Set2 == None):
				global_types.beer_ML_val_Set2 = 0	
			
			global_types.soap_ML_val_Set2 = ML_Model().PredictOutcome(SOAP_ML_IDENTIFIER, instance_soap,\
							str(global_types.checkBox_set_2_0),\
							str(global_types.checkBox_set_2_1))
			if(global_types.soap_ML_val_Set2 == None):
				global_types.soap_ML_val_Set2 = 0	
			global_types.checkBox_set_2_0 = None
			global_types.checkBox_set_2_1 = None
			
			global_types.avg_milk_ML_val = (global_types.milk_ML_val_Set1 + global_types.milk_ML_val_Set2 + global_types.milk_ML_val_Set3)/3
			global_types.avg_beer_ML_val = (global_types.beer_ML_val_Set1 + global_types.beer_ML_val_Set2 + global_types.beer_ML_val_Set3)/3
			global_types.avg_soap_ML_val = (global_types.soap_ML_val_Set1 + global_types.soap_ML_val_Set2 + global_types.soap_ML_val_Set3)/3

class PredictionThread_Set3(object):
	def __init__(self, instance_milk, instance_beer, instance_soap):
		thread = threading.Thread(target=self.StartThread, args = ())
		thread.daemon = True
		thread.start()

	def StartThread(self):
		while True:
			while(global_types.checkBox_set_3_0 == None or global_types.checkBox_set_3_1 == None):
				sleep(1)
				continue
					
			global_types.milk_ML_val_Set3 = ML_Model().PredictOutcome(MILK_ML_IDENTIFIER, instance_milk,\
							str(global_types.checkBox_set_3_0),\
							str(global_types.checkBox_set_3_1))
			if(global_types.milk_ML_val_Set3 == None):
				global_types.milk_ML_val_Set3 = 0
			
			global_types.beer_ML_val_Set3 = ML_Model().PredictOutcome(BEER_ML_IDENTIFIER, instance_beer,\
							str(global_types.checkBox_set_3_0),\
							str(global_types.checkBox_set_3_1))
			if(global_types.beer_ML_val_Set3 == None):
				global_types.beer_ML_val_Set3 = 0	
			
			global_types.soap_ML_val_Set3 = ML_Model().PredictOutcome(SOAP_ML_IDENTIFIER, instance_soap,\
							str(global_types.checkBox_set_3_0),\
							str(global_types.checkBox_set_3_1))
			if(global_types.soap_ML_val_Set3 == None):
				global_types.soap_ML_val_Set3 = 0	
			
			global_types.checkBox_set_3_0 = None
			global_types.checkBox_set_3_1 = None
			
			global_types.avg_milk_ML_val = (global_types.milk_ML_val_Set1 + global_types.milk_ML_val_Set2 + global_types.milk_ML_val_Set3)/3
			global_types.avg_beer_ML_val = (global_types.beer_ML_val_Set1 + global_types.beer_ML_val_Set2 + global_types.beer_ML_val_Set3)/3
			global_types.avg_soap_ML_val = (global_types.soap_ML_val_Set1 + global_types.soap_ML_val_Set2 + global_types.soap_ML_val_Set3)/3


if __name__ == '__main__':
    
	#Initialize global types
	global_types.init()
	
	#Start the Bluetooth Beaconing as a thread
	#example = BluetoothThread()
    
	#Start the trial server
    	trial_zmq_server = zmqServer()
    	#trial_zmq_server.RunZMQServer()
   
	print("HERE!!")
 
	# This is the machine learning API call
	instance_milk = boto3.client('machinelearning',\
						region_name=SERVICE_REGION,\
						aws_access_key_id=AWS_ACCESS_ID,
						aws_secret_access_key=AWS_ACCESS_KEY)
	instance_beer = boto3.client('machinelearning',\
						region_name=SERVICE_REGION,\
						aws_access_key_id=AWS_ACCESS_ID,
						aws_secret_access_key=AWS_ACCESS_KEY)
	instance_soap = boto3.client('machinelearning',\
						region_name=SERVICE_REGION,\
						aws_access_key_id=AWS_ACCESS_ID,
						aws_secret_access_key=AWS_ACCESS_KEY)

	model_ML = ML_Model()
	model_ML.DescribeMLModel(instance_milk)
	model_ML.DescribeMLModel(instance_beer)
	model_ML.DescribeMLModel(instance_soap)

	#Shopping list Qt display	
	gui_application = QtGui.QApplication(sys.argv)
	main_application = GUIApplication()

	#Login Qt display
	#gui_login = QtGui.QApplication(sys.argv)
	#login_application = LoginGUIApplication()	

	# Start the serial input from the Arduino ADC
	#signal.signal(signal.SIGINT, signal_handler)
	#test = fsrThread()
    
	#gui_application = QtGui.QApplication(sys.argv)
	#check_fsr_val = CheckObjectPresence()

	predict_thread = PredictionThread_Set1(instance_milk, instance_beer, instance_soap)	
	predict_thread = PredictionThread_Set2(instance_milk, instance_beer, instance_soap)	
	predict_thread = PredictionThread_Set3(instance_milk, instance_beer, instance_soap)	
	#Show the Shopping list GUI now!
	#login_application.show()

	main_application.show()	
	
	sys.exit(gui_application.exec_())

	while(1 == 1):
		pass	
'''
if __name__ == '__main__':
   
    #Initialize global types
    global_types.init()

    #Start the Bluetooth Beaconing as a thread
    example = BluetoothThread()
    
    # Start the serial input from the Arduino ADC
    signal.signal(signal.SIGINT, signal_handler)
    test = fsrThread()
    
    #check_fsr_val = CheckObjectPresence()


    # This is the machine learning API call
    instance_milk = boto3.client('machinelearning',\
                        region_name=SERVICE_REGION,\
                        aws_access_key_id=AWS_ACCESS_ID,
                        aws_secret_access_key=AWS_ACCESS_KEY)
    instance_beer = boto3.client('machinelearning',\
                        region_name=SERVICE_REGION,\
                        aws_access_key_id=AWS_ACCESS_ID,
                        aws_secret_access_key=AWS_ACCESS_KEY)
    instance_soap = boto3.client('machinelearning',\
                        region_name=SERVICE_REGION,\
                        aws_access_key_id=AWS_ACCESS_ID,
                        aws_secret_access_key=AWS_ACCESS_KEY)

    model_ML = ML_Model()
    model_ML.DescribeMLModel(instance_milk)
    model_ML.DescribeMLModel(instance_beer)
    model_ML.DescribeMLModel(instance_soap)
    prediction_value_milk = model_ML.PredictOutcome(MILK_ML_IDENTIFIER, instance_milk, 'rice', 'nachos')
    prediction_value_beer = model_ML.PredictOutcome(BEER_ML_IDENTIFIER, instance_beer, 'rice', 'nachos')
    prediction_value_soap = model_ML.PredictOutcome(SOAP_ML_IDENTIFIER, instance_soap, 'rice', 'nachos')
    print(prediction_value_milk)
    print(prediction_value_soap)
    print(prediction_value_beer)
    
    #Signal handler for a clean exit on Ctrl+C 
    #signal.signal(signal.SIGINT, signal_handler)
    
    #Start the trial server
    #trial_zmq_server = zmqServer()
    #trial_zmq_server.RunZMQServer()

    while(1 == 1):
        pass
'''
