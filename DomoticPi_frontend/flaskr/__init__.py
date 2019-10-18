from flask import Flask, render_template
from . import utils

import os

app = Flask(__name__)

@app.route('/devices')
def devices():
    data_devices = utils.get_devices()
    return render_template('devices_view.html', data_devices=data_devices)

@app.route('/houses')
def houses():
    data_houses = utils.get_houses()
    return render_template('houses_view.html', data_houses=data_houses)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3001')