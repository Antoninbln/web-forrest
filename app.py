from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/train/upload')
def train_upload():
    
    return render_template('train/upload.html')

@app.route('/train/configure')
def train_configure():
    return render_template('train/configure.html')

# Files to watch