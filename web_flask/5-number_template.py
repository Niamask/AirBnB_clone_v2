#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
/python/<text>: display “Python ”, followed by the value of the text
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    
    # Replace underscores with spaces
    text = text.replace('_',' ')

    # Return the modified text with a prefix
    return "C "+ text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_text(text = "is cool"):

    # Replace underscores with spaces
    text = text.replace('_',' ')

    # Return the modified text with a prefix
    return "Python "+ text


@app.route("/number/<int:n>", strict_slashes=False)
def n_number(n):

    # Check if the n is an integer
    if isinstance(n, int):
        #return n + " is a number"
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_number(n):

    # Display a HTML page only if the n is an integer
    if isinstance(n, int):
        return render_template('5-number.html', n = n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

