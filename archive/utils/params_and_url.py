from archive.models import Image

from flask import abort


def get_params(params):

    dict_params = params_to_dict(params)

    next_url = ""

    for param in dict_params:
        if param == 'count' or param == 'page':
            continue
        next_url = "&" + str(param) + "=" + params[param]

    return next_url


def params_to_dict(params):

    result = {}
    for param in params:
        result[param] = params.get(param, None)

    return result


def image_data_filter(params, datas):

    if not params.get('user_id'):
        abort(401)

    if params.get('title'):
        datas = datas.filter(Image.title == params.get('title'))

    if params.get('artist_name'):
        datas = datas.filter(Image.name == params.get('name'))

    if params.get('year'):
        datas = datas.filter(Image.year == params.get('year'))

    if params.get('description'):
        datas = datas.filter(Image.description == params.get('description'))

    return datas
