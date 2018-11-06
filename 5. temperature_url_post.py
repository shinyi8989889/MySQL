#! /usr/bin/python
#coding=utf-8

import time,datetime
from time import strftime
import urllib

def fetch_thing(url,params,method):
	params = urllib.urlencode(params)
	if method == "POST":
		f = urllib.urlopen(url,params)
	else:
		f = urllib.urlopen(url+"?"+params)
	return(f.read(),f.code)


now=strftime("%H:%M:%S")
file=open("/sys/bus/w1/devices/28-03172164d8ff/w1_slave")
text=file.read()
file.close
secondline = text.split("\n")[1]
tempdata = secondline.split(" ")[9]
temp = float(tempdata[2:])
temp = temp/1000
temp = str(temp)
print temp

content,response_code = fetch_thing(
	"http://192.168.63.9:5000/add_data",
	{"name":"david","quantity":temp},"POST")

