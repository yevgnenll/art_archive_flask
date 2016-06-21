from flask import abort, request

from archive import db, app

from werkzeug import secure_filename

import os


class Image(db.Model):

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    user_id = db.Column(db.String(45))
    thumbnail = db.Column(db.String(255))

    def __repr__(self):
        return '<id:{id} title: {title}>'.format(
            id=self.id,
            title=self.title,
        )

    def data_to_dict(self):

        result_dictionary = {
            "image_url": self.image_url,
            "title": self.title,
            "thumbnail_url": self.thumbnail,
        }

        return result_dictionary

    def data_get_as_dict(self, params_row):

        params = params_row.values
        # from IPython import embed; embed()

        from archive.utils import upload_image_file
        image_path = upload_image_file(params_row)

        self.image_url = request.url_root + image_path.get('origin')
        self.title = params.get('title').replace('\n', '').replace('\r', '')
        self.user_id = params.get('user_id')
        self.thumbnail = request.url_root + image_path.get('thumbnail')

        return self
