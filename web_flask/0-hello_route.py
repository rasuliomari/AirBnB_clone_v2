#!/usr/bin/python3
"""Start a flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return Hello HBNB"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    """stsrt the flask developement server"""
    app.run(host='0.0.0.0', port=5000)
