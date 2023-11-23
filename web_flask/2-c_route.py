#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

