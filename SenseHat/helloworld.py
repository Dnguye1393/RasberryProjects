from sense_hat import SenseHat
from flask import Flask, render_template, jsonify, request

import requests
app = Flask(__name__)

sense = SenseHat()

languages =[{'name':'JavaScript'}, {'name':'Python'}, {'name':'Java'}]

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
    language ={'name': request.json['name']}
    languages.append(language)
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
    languages.remove(langs[0])
    return jsonify({'language':languages})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
