import jwt
from datetime import datetime, timedelta
from flask import current_app
from passlib.hash import bcrypt

def hash_password(password):
    return bcrypt.hash(password)

def verify_password(password, password_hash):
    return bcrypt.verify(password, password_hash)

def create_token(user_id, expires_seconds=None):
    secret = current_app.config['JWT_SECRET']
    exp = datetime.utcnow() + timedelta(seconds=expires_seconds or current_app.config.get('JWT_EXPIRATION_SECONDS'))
    payload = {"sub": user_id, "exp": exp}
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

def decode_token(token):
    secret = current_app.config['JWT_SECRET']
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise
    except Exception:
        raise
