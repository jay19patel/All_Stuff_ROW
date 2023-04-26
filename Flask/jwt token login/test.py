from flask_jwt_extended import create_access_token,set_access_cookies,get_jwt_identity

def LoginPage():
    access_token = create_access_token(identity='jay')
    res = jso(url_for('HomePage'))
    set_access_cookies(res, access_token) 
    return res
               


def redirect():
    data = get_jwt_identity()
    if 'identity' in data:
        authorized = True
    else:
        authorized = False