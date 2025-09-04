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


p = 1331169830894825846283645180581
a = -35
b = 98
G = (479691812266187139164535778017 , 568535594075310466177352868412)

n = 29618469991922269
B = Point(1290982289093010194550717223760, 762857612860564354370535420319)
shared_secret_point = double_and_add(n, B, a, p)
shared_secret = shared_secret_point[0]
data = {'iv': 'eac58c26203c04f68d63dc2c58d79aca', 'encrypted_flag': 'bb9ecbd3662d0671fd222ccb07e27b5500f304e3621a6f8e9c815bc8e4e6ee6ebc718ce9ca115cb4e41acb90dbcabb0d'}
decrypted = decrypt_flag(shared_secret, data)
print("Decrypted:", decrypted.decode())