from flask import render_template, request, jsonify, abort
from sqlalchemy.orm import sessionmaker

from archive import app
from archive.models import Image

from archive.utils import pagination_dict, image_data_filter,\
    pagination_for_list


@app.route('/api/images/', methods=['GET'])
def images():

    images = Image.query
    images = image_data_filter(request.args, images)

    list_amount = images.count()

    images = pagination_for_list(request.args, images)

    content = []
    for image in images:
        data = image.data_to_dict()
        content.append(data)

    return jsonify(
        content=content,
        code=200,
        pagination=pagination_dict(request.args, list_amount),
    )


@app.route('/api/images/', methods=['POST'])
def images_insert():

    is_check = is_title_artist_exist(request.values)
    if not is_check:
        abort(400)

    image = Image()
    Image.query.session.add(
        image.data_get_as_dict(request)
    )

    Image.query.session.commit()

    return jsonify(
        code=201,
        content={'result': 'Created'},
    )


@app.route('/api/images/<id>', methods=['GET'])
def images_detail(id):

    image = Image.query.get_or_404(id)
    # name = Artist.query.filter(Artist.id == image.artist_id)

    content = image.data_to_dict(
        name.one().name,
    )

    return jsonify(
        code=200,
        content=content,
    )


@app.route('/api/images/<id>', methods=['PUT'])
def images_update(id):

    print('image update')
    # from IPython import embed; embed()
    params = request.values
    image = Image.query.filter(Image.id == id)

    if not images.all():
        abort(404)
    image.update(params)

    Image.query.session.commit()

    return jsonify(
        code=200,
        content={"result": "OK"},
    )


@app.route('/api/images/<id>', methods=['DELETE'])
def images_delete(id):

    image = Image.query.filter(Image.id == id)

    if not image.all():
        abort(404)

    image.delete()

    Image.query.session.commit()

    return jsonify(
        code=204,
        content={"result": "No Content"},
    )
