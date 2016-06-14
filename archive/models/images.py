from flask import abort, request

from archive import db, app

from werkzeug import secure_filename

import os


class Image(db.Model):

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    artist_name = db.Column(db.String(150))
    description = db.Column(db.String(255))
    user_id = db.Column(db.String(45))

    def __repr__(self):
        return '<id:{id} title: {title}>'.format(
            id=self.id,
            title=self.title,
        )

    def data_to_dict(self):

        result_dictionary = {
            "id": self.id,
            "image_url": self.image_url,
            "title": self.title,
            "year": self.year,
            "artist_name": self.artist_name,
            "description": self.description,
            "user_id": self.user_id,
        }

        return result_dictionary

    def data_get_as_dict(self, params_row):

        params = params_row.values
        year = params['year']
        # from IPython import embed; embed()
        print(params)
        for key in params:
            if key == 'image_file':
                print(key, '-----')
            print(key, ":", params[key])
        for key in params_row:
            if key == 'iamge_file':
                print(key)
            print('----', key, ": ", params_row[key])

        try:
            year = int(year)
        except ValueError:
            # abort(400)
            pass

        from archive.utils import upload_image_file
        image_path = upload_image_file(params_row)

        self.year = year
        self.image_url = request.url_root + image_path
        self.title = params['title']
        self.artist_name = params['artist_name']
        self.description = params['description']
        self.user_id = params['user_id']

        return self
