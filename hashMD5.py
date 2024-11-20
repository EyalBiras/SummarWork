import hashlib

def hash_md5(password: bytes) -> str:
    return hashlib.md5(password).hexdigest()
