""" A script that starts Flask web application """

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ This prints the web """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ This prints the web """
    return 'HBNB'

@app.route('/c/<text>')
def c_is_fun():   
    """ Displays char C flollowed by what the variable <text> holds """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text="is cool"):
    """ Displays "Python" followed by the value of 'text' variable
    with the default value of text "is cool"
    """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def is_n_number(n):
    """ Displays 'n is a number only if n is an integer' """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
