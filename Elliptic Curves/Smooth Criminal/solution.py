import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from collections import namedtuple
import hashlib
from Crypto.Util.number import inverse


def point_addition(P, Q, a, p):
    if P == "O":
        return Q
    if Q == 'O':
        return P
    
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2  and (y1 + y2) % p == 0:
        return "O"
    if P != Q:
        lmbd = (y2 - y1) * inverse(x2 - x1, p) % p
    else:
        lmbd = (3 * x1**2 + a) * inverse(2 * y1, p) % p

    x3 = (lmbd**2 - x1 - x2) % p
    y3 = (lmbd * (x1 - x3) - y1) % p

    return (x3, y3)


def double_and_add(n, P, a, p):
    R = 'O'  
    Q = P
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q, a, p)
        Q = point_addition(Q, Q, a, p)
        n = n // 2
    return R

Point = namedtuple("Point", "x y")

def decrypt_flag(shared_secret: int, data: dict) -> bytes:
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    
    iv = bytes.fromhex(data['iv'])
    ciphertext = bytes.fromhex(data['encrypted_flag'])
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), 16)
    
    return plaintext

n= 47836431801801373761601790722388100620 # from sage math
p = 310717010502520989590157367261876774703
a = 2
b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317
B = Point(b_x, b_y)
shared_secret_point = double_and_add(n, B, a, p)
shared_secret = shared_secret_point[0]
data = {'iv': '07e2628b590095a5e332d397b8a59aa7', 'encrypted_flag': '8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af'}
decrypted = decrypt_flag(shared_secret, data)
print("Decrypted:", decrypted.decode())