#!/usr/bin/python
#coding=utf-8

from flask import Flask,redirect,url_for,request

import mysql.connector
from mysql.connector import errorcode

app=Flask(__name__)

@app.route('/add_data',methods=['POST','GET'])
def add_data():
    config={'host':'localhost',
            'user':'root',
            'passwd':'1234',
            'database':'mydatabase'}
    try:
        conn=mysql.connector.connect(**config)
        print "connection established"

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "something is wrong with the user name or passwd"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist"
        else:
            print err
    else:
        cursor = conn.cursor()
#################################################################
        if request.method == "POST":
            fruit = request.form['fruitname']
            quantity = request.form['quantity']
            #insert some data into table
            cursor.execute("INSERT INTO inventory (name,quantity) VALUES (%s,%s)",(fruit,quantity))
            print "Inserted",cursor.rowcount,"row(s) of data."

            conn.commit()
            #clearup
            cursor.close()
            conn.close()
            print "POST Done."

            return redirect(url_for('index'))
        else:
            fruit = request.args.get('fruitname')
            quantity = request.args.get('quantity')
            #insert some data into table
            cursor.execute("INSERT INTO inventory (name,quantity) VALUES (%s,%s)",(fruit,quantity))
            print "Inserted",cursor.rowcount,"row(s) of data."

            conn.commit()
            #clearup
            cursor.close()
            conn.close()
            print "GET Done."

            return redirect(url_for('index'))

@app.route('/update_data',methods=['POST','GET'])
def update_data():
    config={'host':'localhost',
            'user':'root',
            'passwd':'1234',
            'database':'mydatabase'}
    try:
        conn=mysql.connector.connect(**config)
        print "connection established"
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "something is wrong with the user name or passwd."
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist."
        else:
            print err
    else:
        cursor = conn.cursor()
##################################################################
        if request.method == "POST":
            fruitid = request.form['fruitid']
            fruit = request.form['fruitname']
            quantity = request.form['quantity']
            #insert some data into table
            if len(str(fruitid))==0:
                cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s",(quantity,fruit))
            else:
                cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s AND id = %s",(quantity,fruit,fruitid))
            print "Updated "+str(cursor.rowcount)+ " row(s) of data."

            conn.commit()
            #clearup
            cursor.close()
            conn.close()
            print "POST Done."

            return redirect(url_for('index'))

        else:
            fruit = request.args.get('fruitname')
            quantity = request.args.get('quantity')
            fruitid = request.args.get('fruitid')
            #insert some data into table
            if len(str(fruitid))==0:
                cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s",(quantity,fruit))
            else:
                cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s AND id = %s",(quantity,fruit,fruitid))
            print "Updated "+str(cursor.rowcount)+" row(s) of data."

            conn.commit()
            #clearup
            cursor.close()
            conn.close()
            print "GET Done."

            return redirect(url_for('index'))


@app.route('/delete_data',methods=['POST','GET'])
def delete_data():
    config={'host':'localhost',
            'user':'root',
            'passwd':'1234',
            'database':'mydatabase'}
    try:
        conn = mysql.connector.connect(**config)
        print "connection established"
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "something is wrong with the user name or passwd"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist"
        else:
            print err
    else:
        cursor = conn.cursor()
######################################################################
        if request.method == "POST":
            fruit = request.form['fruitname']
            fruitid = request.form['fruitid']
            quantity = request.form['quantity']
            #insert some data into table
            if len(str(fruit))!=0 and len(str(fruitid))!=0:
                cursor.execute("DELETE FROM inventory WHERE name = %s AND id = %s",(fruit,fruitid))
            else:
                cursor.execute("DELETE FROM inventory WHERE id = %s",(fruitid,))
                cursor.execute("DELETE FROM inventory WHERE name = %s",(fruit,))
            print "Delete "+str(cursor.rowcount)+" row(s) of data."

            conn.commit()
            #clearup
            cursor.close()
            conn.close()
            print "POST Done."

            return redirect(url_for('index'))
        else:
            fruit = request.args.get('fruitname')
            fruitid = request.args.get('fruitid')
            quantity = request.args.get('quantity')
            #insert some data into table
            if len(str(fruit))!=0 and len(str(fruitid))!=0:
                cursor.execute("DELETE FROM inventory WHERE name = %s AND id = %s",(fruit,fruitid))
            else:
                cursor.execute("DELETE FROM inventory WHERE id = %s",(fruitid,))
                cursor.execute("DELETE FROM inventory WHERE name = %s",(fruit,))
            print "Delete " + str(cursor.rowcount)+" row(s) of data."

            conn.commit()
            #clearup
            cursor.close()
            conn.close()
            print "GET Done."

            return redirect(url_for('index'))

@app.route('/')
def index():
    return "You did something but anyway you Well Done!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
