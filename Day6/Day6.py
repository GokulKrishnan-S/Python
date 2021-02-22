'''
Day 6 Template
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/developers/<string:name>')
def developer(name=None):
    return render_template('dev.html', name=name)
    