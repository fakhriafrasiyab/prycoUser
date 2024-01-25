import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashedPassword: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashedPassword.encode('utf-8'))