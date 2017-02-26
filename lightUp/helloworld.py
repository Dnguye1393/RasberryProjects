from flask import Flask, render_template
from turnon import runOn
from turnoff import runOff
app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html', title="Home Page")

@app.route('/lighton')
def lighton():
    runOn()
    print ('I got Clicked')
    return render_template('lighton.html' , title="Light On")

@app.route('/lightoff')
def lightoff():
    runOff()
    return render_template('lightoff.html', title="Light Off")


def format(value):
    return "%.3f" % value

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
