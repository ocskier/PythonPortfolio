from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates');

@app.route('/')
def serveHomePage(): 
    html = open(os.path.join(os.path.dirname(__file__), './templates/index.html'),mode='r').read()
    print(html)
    return html

