import jwt
import datetime

ALGORITHM="HS256"

SECRET_KEY = "0a6dd#j4F005F8Hed20934df3$l"

def create_token(data, expiration_minutes=1):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
    payload = {"exp": expiration_time, 'data':data}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid token.")