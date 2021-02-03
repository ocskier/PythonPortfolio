from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def serveHomePage(): 
    return render_template('index.html')

@app.route('/about')
def serveAboutPage(): 
    return render_template('about.html', name='Jon')

