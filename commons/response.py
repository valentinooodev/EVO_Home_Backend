def default_response(data, message=''):
    response = dict()
    response['data'] = data
    if message != '':
        response['message'] = message
    return response
