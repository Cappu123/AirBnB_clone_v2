""" Script that starts web application, must lilsten to 0.0.0.0:5000 """

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """prints the web"""
    return "Hello HBNB!"
@app.route('/hbnb')
def hbnb():
    """prints the hbnb"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
