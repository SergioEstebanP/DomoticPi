from flask import Flask, render_template
import os

app = Flask(__name__)

# TODO move this to 
PORT = 3000
LOCALHOST = '0.0.0.0'

@app.route('/index')
def devices():
    return render_template('main_view.html')

if __name__ == '__main__':
    app.run(debug=True, host=LOCALHOST, port=PORT)
