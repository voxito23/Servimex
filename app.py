import os
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-key')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('services.html')

@app.route('/contacto')
def contacto():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
