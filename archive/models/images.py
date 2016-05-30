from archive import db

from archive.models import Artist


class Image(db.Model):

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<id:{id} title: {title}>'.format(
            id=self.id,
            title=self.title,
        )

    def data_to_dict(self, artist_name):

        result_dictionary = {
            "id": self.id,
            "image_url": self.image_url,
            "title": self.title,
            "year": self.year,
            "artist_id": self.artist_id,
            "description": self.description,
            "name": artist_name,
        }

        return result_dictionary

    def data_get_as_dict(self, params):

        year = params['year']

        try:
            year = int(year)
        except ValueError:
            abort(400)

        self.year = year
        self.image_url = params['image_url']
        self.title = params['title']
        self.artist_id = params['artist_id']
        self.description = params['description']

        return self
