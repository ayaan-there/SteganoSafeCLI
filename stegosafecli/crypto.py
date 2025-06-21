"""
AES encryption/decryption for messages using pycryptodome.
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

def _get_key(key_str, mode):
    if mode == 'AES-128':
        return hashlib.sha256(key_str.encode()).digest()[:16]
    elif mode == 'AES-256':
        return hashlib.sha256(key_str.encode()).digest()
    else:
        raise ValueError('Invalid AES mode')

def encrypt_message(message, key, mode):
    key_bytes = _get_key(key, mode)
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f'{iv}:{ct}'

def decrypt_message(enc_message, key, mode):
    key_bytes = _get_key(key, mode)
    iv, ct = enc_message.split(':')
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')
