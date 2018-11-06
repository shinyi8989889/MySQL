#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask, render_template
from flask import request, url_for

import mysql.connector
from mysql.connector import errorcode

import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/add_data', methods=['GET','POST'])
def add_data():

	if request.method == 'GET':
		name = str(request.args.get('name'))
		quantity = str(request.args.get('quantity'))
	else:
		name = str(request.form["name"])
		quantity = str(request.form["quantity"])
		# Obtain connection string information from the portal
	
	config = {
		'host':'localhost',
		'user':'root',
		'password':'1234',
		'database':'mydatabase'
	}

	# Construct connection string
	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print "Something is wrong with the user name or password"
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print "Database does not exist"
		else:
			print err
	else:
		cursor = conn.cursor()
		sql_query = ("INSERT INTO inventory (name, quantity) VALUES (%s, %s)")
		cursor.execute(sql_query, (name, quantity))
		conn.commit()
		print("Inserted",cursor.rowcount,"row(s) of data.")

		#Cleanup
		cursor.close()
		conn.close()
		print("Done.")
		return "You did add Something is successful no worry haha"
############################################################################################

@app.route('/update_data', methods=['GET','POST'])
def update_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))
		name = str(request.args.get('name'))
		quantity = str(request.args.get('quantity'))
	else:
		user_id = str(request.form["id"])
		name = str(request.form["name"])
		quantity = str(request.form["quantity"])
	
	# Obtain connection string information from the portal
	config = {
		'host':'localhost',
		'user':'root',
		'password':'1234',
		'database':'mydatabase'}		
	
	# Construct connection string
	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print "Something is wrong with the user name or password"
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print "Database does not exist"
		else:
			print err
	else:
		cursor = conn.cursor()
		# cursor.execute("UPDATE inventory SET quantity = %s, name = %s WHERE id = %s;",(quantity,name,user_id))
		sql_query = "UPDATE inventory SET quantity = %s, name = %s WHERE id = %s;"
		cursor.execute(sql_query,(quantity,name,user_id))
		conn.commit()

		#Cleanup
		cursor.close()
		conn.close()
		return "update ok"
############################################################################################
@app.route('/select_data', methods=['GET','POST'])
def select_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))
	else:
		user_id = str(request.form["id"])
	
	# Obtain connection string information from the portal
	config = {
		'host':'localhost',
		'user':'root',
		'password':'1234',
		'database':'mydatabase'}			

	# Construct connection string
	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print "Something is wrong with the user name or password"
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print "Database does not exist"
		else:
			print err
	else:
		cursor = conn.cursor(dictionary=True)
		#cursor=conn.cursor()
		sql_query = "SELECT * FROM inventory WHERE id = %s;"
		cursor.execute(sql_query,(user_id,))
		rows = cursor.fetchall()
		# print type(rows)
		# print rows

		data_string = json.dumps(rows)
		#print data_string
		
		#Cleanup
		cursor.close()
		conn.close()
		return data_string
############################################################################################
@app.route('/delete_data', methods=['GET','POST'])
def delete_data():
	if request.method == 'GET':
		user_id = str(request.args.get('id'))
	else:
		user_id = str(request.form["id"])
	
	# Obtain connection string information from the portal
	config = {
		'host':'localhost',
		'user':'root',
		'password':'1234',
		'database':'mydatabase'}				

	# Construct connection string
	try:
		conn = mysql.connector.connect(**config)
		print("Connection established")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print "Something is wrong with the user name or password"
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print "Database does not exist"
		else:
			print err
	else:
		cursor = conn.cursor()
		sql_query = "DELETE FROM inventory WHERE id = %s;"
		cursor.execute(sql_query,(user_id,))
		conn.commit()

		#Cleanup
		cursor.close()
		conn.close()
		return "delete ok"
############################################################################################

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
