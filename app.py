import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/credit')
def credit():
    return render_template('credit.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/learn/')
def learn():
    return render_template('learn.html')

@app.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/requirement/')
def requirement():
    return render_template('requirement.html')

@app.route('/testimonials/')
def testimonials():
    return render_template('testimonials.html')

@app.route('/transport/')
def transport():
    return render_template('transport.html')

if __name__ == "__main__":
    app.run(debug=True)