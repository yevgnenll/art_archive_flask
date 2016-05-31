from archive import app, BASE_DIR

from flask import render_template, send_from_directory

from archive.models import Artist
from archive.models import Image

import os


@app.route('/')
def index():

    return render_template(
        'home.html',
    )

@app.route('/uploads/<filename>')
def access_upload_image(filename):
    print("base_dir", BASE_DIR)

    return send_from_directory(
        os.path.join(
            BASE_DIR,
            app.config['UPLOAD_FOLDER'],
        ),
        filename,
    )
