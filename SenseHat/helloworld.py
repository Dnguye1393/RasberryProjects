from sense_hat import SenseHat
from flask import Flask, render_template
app = Flask(__name__)
sense = SenseHat()

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


def format(value):
    return "%.3f" % value

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
