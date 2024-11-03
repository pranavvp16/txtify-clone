from flask import Flask, render_template
import regex as re
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<path:url>')
def scrape(url):
    # Import required module
    from txtify import Txtify

    # Create an instance of Txtify
    txtify = Txtify(url)
    text = txtify.run()

    return render_template('index.html', text=text)