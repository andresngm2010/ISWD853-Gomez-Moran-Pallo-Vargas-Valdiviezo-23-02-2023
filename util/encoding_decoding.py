from cryptography.fernet import Fernet

key=b'Jws2KcHNH4lLfXsgyy1SgDGs0TY2m6U5w7OxllF53UU='

def encrypted(password:str):
    b_password = bytes(password, 'ascii')
    f = Fernet(key)
    encrypted_password = f.encrypt(b_password)
    return encrypted_password.decode('ascii')

def decrypt(password:str):
    b_password = bytes(password, 'ascii')
    f = Fernet(key)
    b_password_decrypt = f.decrypt(b_password)
    return b_password_decrypt.decode('ascii')