from flask import Flask, render_template
import regex as re
app = Flask(__name__)

def wrap_text(text, width=70):
    lines = []
    current_line = ""

    for word in text.split():
        # Check if adding the next word would exceed the width
        if len(current_line) + len(word) + 1 > width:
            # If yes, add the current line to lines and start a new line
            lines.append(current_line)
            current_line = word
        else:
            # Otherwise, add the word to the current line
            if current_line:
                current_line += " "
            current_line += word

    # Add the last line if there's any remaining text
    if current_line:
        lines.append(current_line)

    return "\n".join(lines)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<path:url>')
def scrape(url):
    # Import required module
    from txtify import Txtify

    # Create an instance of Txtify
    txtify = Txtify(url)
    content = txtify.run()

    return render_template('index.html', text=content)