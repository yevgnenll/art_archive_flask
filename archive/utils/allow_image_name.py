from flask import abort

from archive import app, BASE_DIR

from werkzeug import secure_filename

import time
import os


def is_allowed_extend(filename):

    return '.' in filename and \
        filename.split('.').pop() in app.config['ALLOWED_EXTENSIONS']


def save_upload_file(upload_file, result_name):

    upload_file.filename = result_name
    upload_file.save(
        os.path.join(
            BASE_DIR,
            app.config['UPLOAD_FOLDER'],
            result_name,
        )
    )


def upload_image_file(data):

    upload_file = data.files['image_file']
    file_name = upload_file.filename

    if not is_allowed_extend(file_name):
        abort(400)

    # make current time as image name
    pre_name = str(time.time()).split('.')[0]
    ext_name = file_name.split('.').pop()

    result_name = secure_filename(
        '.'.join([pre_name, ext_name])
    )

    save_upload_file(upload_file, result_name)

    return 'uploads/' + result_name
