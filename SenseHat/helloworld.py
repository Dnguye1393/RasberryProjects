from sense_hat import SenseHat
from flask import Flask, render_template
app = Flask(__name__)
sense = SenseHat()

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/my-link/')
def my_link():

    sense.show_message("hello world!")
    print ('I got Clicked')
    return 'Click.'

@app.route('/get-temp/')
def get_temp():
    temp = sense.get_temperature()
    print("Temperature: %s C",  temp)
    f = open('test.txt','w')
    f.write("Temperature: " +  format(temp) + " C")
    f.close()
    return "Tempterature "


def format(value):
    return "%.3f" % value

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
