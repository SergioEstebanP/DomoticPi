from flask import Flask, render_template
from . import utils

import os

app = Flask(__name__)

@app.route('/devices')
def devices():
    data = utils.get_devices()
    return render_template('main_view.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3000')