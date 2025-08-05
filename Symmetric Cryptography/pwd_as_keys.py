from Crypto.Cipher import AES
import hashlib
import requests
from binascii import hexlify

r = requests.get("http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/")
ct = (r.text).split('"')[3]

with open("pws_as_keys_wl.txt") as f:
    words = [w.strip() for w in f.readlines()]

def decrypt(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

for i in words:
    KEY = hashlib.md5(i.encode()).digest()
    pt = decrypt(ct, KEY)
    if b"crypto{" in pt:
        print (KEY)
        print(pt.decode())