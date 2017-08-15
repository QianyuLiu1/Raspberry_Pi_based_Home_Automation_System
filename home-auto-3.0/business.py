from controlLed import turn_on_led
from controlLed import turn_off_led
from readConfig import read
from os import system
import ctypes

def controlLed(device, value):
	mapping = read()
	number = mapping[device]

	if value == 'on': #on
		turn_on_led(number)
	elif value == 'off': #off
		turn_off_led(number)

def getSensor_Data(device):
	#get from dht11
	so = ctypes.cdll.LoadLibrary('./libsensor.so')
	data = so.getData()
	return data

def getVideo_IP():
	f= open("ip-config.txt") 
   	ip = f.readline()
   	return ip

def startVideo():
	#cmd = '/usr/local/bin/mjpg_streamer -i "/usr/local/lib/input_uvc.so -y" -o "/usr/local/lib/output_http.so -w /usr/local/www"'
	#system(cmd)
	print('start video')




