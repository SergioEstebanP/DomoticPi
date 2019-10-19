from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/index')
def devices():
    return render_template('main_view.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3000')