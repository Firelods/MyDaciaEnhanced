from functools import wraps

import jwt
from flask import request, g

from api.account import SECRET_KEY, cipher_suite
from api.database import postgres_db


def token_required():
    token = request.headers.get('Authorization').split(" ")[1]
    if token is None:
        raise Exception("Token manquant")
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        return decoded_token["login_id"]
    except:
        raise Exception("Token invalide")
