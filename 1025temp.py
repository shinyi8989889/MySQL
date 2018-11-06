#! /usr/bin/python
#coding=utf-8

import mysql.connector
from mysql.connector import errorcode

import time,datetime
from time import strftime

#obtain connection string information
config={'host':'localhost',
        'user':'root',
        'passwd':'1234',
        'database':'IOT'}

#construct connect string
try:
    conn=mysql.connector.connect(**config)
    print"connection established"
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print "sometihing is wrong with the user name or passwd."
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print "Database does not exist."
    else:
        print err
else:
    cursor = conn.cursor()
    now = strftime("%Y/%m/%d %H:%M:%S")
    file = open("/sys/bus/w1/devices/28-03172164d8ff/w1_slave")
    text = file.read()
    file.close

    secondline = text.split("\n")[1]
    tempdata = secondline.split(" ")[9]
    temp = float(tempdata[2:])

    temp = temp//100
    temp = temp/10

    cursor.execute("INSERT INTO temperature_DB(userid,temperature,`datetime`)VALUES(7,%s,%s)",(str(temp),now))
    print "Inserted "+str(cursor.rowcount)+" row(s) of data."
    
    conn.commit()
    #clearup
    cursor.close()
    conn.close()
    print "Done."


#mycursor = temp.cursor()
#mycursor.execute("CREATE DATABASE IOT CHARACTER SET utf8 COLLATE utf8_unicode_ci")
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#    print x

#mycursor.execute("CREATE TABLE temperature_DB(ID serial PRIMARY KEY,userid INT, temperature float, datetime datetime)")


#close
#temp.close()


