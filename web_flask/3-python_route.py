""" Script thet starts flask web application """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """ Prints the web """
    return 'Hello_HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Prints the web """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Prints 'C' followed by what is passed inside the 'text' variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python(text = 'is cool'):
    """ Prints 'Python' followed by what is passed inside 'text' variable
    default value of 'text' is "is cool" """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
