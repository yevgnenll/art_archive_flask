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

    if params.get('user_id'):
        datas = datas.filter(Image.user_id == params.get('user_id'))
    else:
        abort(404)

    return datas
