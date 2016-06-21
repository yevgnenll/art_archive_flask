from flask import abort, request

from archive import app, BASE_DIR

from werkzeug import secure_filename
from PIL import Image

import time
import os


def is_allowed_extend(filename):

    return '.' in filename and \
        filename.split('.').pop() in app.config['ALLOWED_EXTENSIONS']


def save_to_server(upload_file, result_name):

    upload_file.filename = result_name
    upload_file.save(
        os.path.join(
            BASE_DIR,
            app.config['UPLOAD_FOLDER'],
            result_name,
        )
    )


def create_thumbnail(upload_file, file_name):

    size = (100, 100)

    try:
        im = Image.open(upload_file)
        im.thumbnail(size)
        result_name = "thumbnail_" + file_name
        save_to_server(im, result_name)
        im.close()
    except IOError:
        abort(400)
    return 'uploads/' + result_name


def upload_image_file(data):

    upload_file = data.files.get('image_data')
    file_name = upload_file.filename

    if not is_allowed_extend(file_name):
        abort(400)

    # make current time as image name
    # 134563322.232 -> 134563322
    pre_name = str(time.time()).split('.')[0]
    ext_name = file_name.split('.').pop()

    result_name = secure_filename(
        '.'.join([pre_name, ext_name])
    )

    thumbnail = create_thumbnail(upload_file, result_name)
    save_to_server(data.files.get('image_data'), result_name)

    return {
        'origin': 'uploads/' + result_name,
        'thumbnail': thumbnail,
    }
