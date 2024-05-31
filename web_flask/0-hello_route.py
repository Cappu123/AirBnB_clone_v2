#!/usr/bin/python3
"""
a script that starts a Flask web application
the  web application must be listening on 0.0.0.0, port 5000
/: display /: display "Hello HBNB!"
must use the option strict_slashes=False in the route definition

"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
