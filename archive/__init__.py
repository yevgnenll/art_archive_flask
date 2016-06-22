from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename

import os


app = Flask(__name__)
app.config.from_object('config')
# app.wsgi_app = MethodRewriteMiddleware(app.wsgi_app)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(
    ['png', 'jpg', 'gif', 'jpeg', 'bmp', 'svg']
)

db = SQLAlchemy(app)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


from archive import views
