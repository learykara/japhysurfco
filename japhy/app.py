
import os

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', selectedClass='home')

@app.route('/our-story')
def ourstory():
	return render_template('our-story.html', selectedClass='our-story')

@app.route('/products')
def products():
	return render_template('products.html', selectedClass='products')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html', selectedClass='gallery')

@app.route('/purchase')
def purchase():
	return render_template('purchase.html', selectedClass='purchase')

@app.route('/contact-us')
def contact():
	return render_template('contact-us.html', selectedClass='contact-us')

if __name__ == '__main__':
    app.run(debug=True)