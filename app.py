from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def serveHomePage(): 
    return render_template('home.html', name='Jon Jackson')

@app.route('/about')
def serveAboutPage(): 
    return render_template('about.html')

@app.route('/portfolio')
def servePortfolioPage(): 
    return render_template('portfolio.html')

if (__name__ == '__main__'): 
    app.run(debug=True)

