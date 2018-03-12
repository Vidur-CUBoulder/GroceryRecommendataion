def init():

	global gl_ble_address
	gl_ble_address = 0

	global gl_ble_rssi_val
	gl_ble_rssi_val = 0

	global gl_adc_sensor_val
	gl_adc_sensor_val = 0

	global gl_picked
	gl_picked = False

	global gl_mqttc

	global gl_numItem
	gl_numItem = 0

	global end_point_url
	end_point_url = 0

	global volume
	volume = 100

	global stupid_ret_val
	stupid_ret_val = False

	global checkBox_set_1_0
	checkBox_set_1_0 = None 
	global checkBox_set_1_1
	checkBox_set_1_1 = None
	global checkBox_set_2_0 
	checkBox_set_2_0 = None
	global checkBox_set_2_1 
	checkBox_set_2_1 = None
	global checkBox_set_3_0 
	checkBox_set_3_0 = None
	global checkBox_set_3_1 
	checkBox_set_3_1 = None

	global avg_milk_ML_val
	avg_milk_ML_val = 0
	global avg_beer_ML_val
	avg_beer_ML_val = 0
	global avg_soap_ML_val
	avg_soap_ML_val = 0 

	global milk_ML_val_Set1
	milk_ML_val_Set1 = 0
	global milk_ML_val_Set2
	milk_ML_val_Set2 = 0
	global milk_ML_val_Set3
	milk_ML_val_Set3 = 0
 
	global beer_ML_val_Set1
	beer_ML_val_Set1 = 0
	global beer_ML_val_Set2
	beer_ML_val_Set2 = 0
	global beer_ML_val_Set3
	beer_ML_val_Set3 = 0

	global soap_ML_val_Set1
	soap_ML_val_Set1 = 0
	global soap_ML_val_Set2
	soap_ML_val_Set2 = 0
	global soap_ML_val_Set3
	soap_ML_val_Set3 = 0

