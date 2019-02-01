import os

from flask import Flask
from flask import render_template, redirect, request
from forms import UploadTrainForm

UPLOAD_PATH = 'storage'

app = Flask(__name__)

# Add CSRF tokens
app.config.update(dict(
    SECRET_KEY=os.urandom(32),
    WTF_CSRF_SECRET_KEY=os.urandom(32)
))



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/train/upload', methods=('GET', 'POST'))
def train_upload():
    form = UploadTrainForm()

    # Validate form
    if form.validate_on_submit():
        #Do something here...
        file = request.files[form.dataset.name]
        open(os.path.join(UPLOAD_PATH, file.filename), 'wb').write(file.read())

        return redirect('/train/configure')

    # Render form view
    return render_template('train/upload.html', form=form)

@app.route('/train/configure')
def train_configure():
    return render_template('train/configure.html')

# Files to watch