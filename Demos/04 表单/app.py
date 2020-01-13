# -*- coding: utf-8 -*-

import os
from forms import LoginForm, UploadForm
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'aewfwaefwaefwa'
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')


@app.route('/basic')
def basic():
    form = LoginForm()
    return render_template('basic.html', form=form)




