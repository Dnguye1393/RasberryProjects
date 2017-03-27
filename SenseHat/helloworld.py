from sense_hat import SenseHat
from flask import Flask, render_template, jsonify, request
import mysql.connector
from mysql.connector import MySQLConnection, Error
import requests
app = Flask(__name__)

sense = SenseHat()
languages = []
cnx = mysql.connector.connect(user = 'davidn', password='raspberry' ,
                                host='localhost', database='senseHat')
cursor = cnx.cursor()
cursor.execute("SELECT name from languages")
data = cursor.fetchall()
for row in data :
    language ={'name': row[0]}
    languages.append(language)
    print ('Adding to Languages')

@app.route('/')
def index():

    return render_template('index.html', title="Home Page")

@app.route('/helloWorld')
def my_link():

    sense.show_message("hello world!")
    print ('I got Clicked')
    return render_template('helloWorld.html' , title="Hello World")

@app.route('/temperature')
def get_temp():
    temp = sense.get_temperature()
    print("Temperature: %s C",  temp)
    f = open('test.txt','w')
    f.write("Temperature: " +  format(temp) + " C")
    f.close()
    return render_template('temperature.html', title="Temperature")

@app.route('/restget' , methods=['GET'])
def test():
    return jsonify({'languages':languages})

@app.route('/restget' , methods=['POST'])
def addOne():
    val = request.json['name']
    alreadyExist = False
    for language in languages :
        if ( language['name']==val ) :
            alreadyExist = True
    if(not alreadyExist) :
        language ={'name': val}
        languages.append(language)
        sql = 'INSERT INTO languages(name) VALUES("%s")' % (val)
        try:
            cursor.execute(sql)
            cnx.commit()
        except Error as error:
                print(error)
    else :
        print("This value, ", val, ", already exists" )
    return jsonify({'languages':languages})

@app.route('/restget/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name']==name]
    return jsonify({'language':langs[0]})



@app.route('/restget/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name']==name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language':langs[0]})

@app.route('/restget/<string:name>', methods=['DELETE'])
def deleteOne(name):
    langs = [language for language in languages if language['name']==name]
    alreadyExist = False
    val = langs[0]
    for language in languages :
        if ( language['name']==val ) :
            alreadyExist = True
    if(alreadyExist) :
        languages.remove(langs[0])
        sql ='DELETE FROM languages WHERE name = %s' % (val)
        try:
            cursor.execute(sql)
            cnx.commit()
        except Error as error:
                print(error)
    else :
        print("This value, ", val, ", does not exists" )
    return jsonify({'language':languages})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
