
import jwt
from flask import request

from account import SECRET_KEY


def token_required():
    try:
        token = request.headers.get('Authorization').split(" ")[1]
    except:
        raise Exception("Token manquant")
    if token is None:
        raise Exception("Token manquant")
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        return decoded_token["login_id"]
    except:
        raise Exception("Token invalide")
