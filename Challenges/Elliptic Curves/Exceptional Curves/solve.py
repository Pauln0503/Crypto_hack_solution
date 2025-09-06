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

p = 8451139905551902831160354990243448994735923344327179631310525520435196861496551764162970081762137226285330762159796842785356834064520159547540428116601719
a = 4923298572065486992549817192831990694521484100405815221208729152906589637309679506395496485479241352604070239922404839767350734501408775691888115823029570
b = 2351894222324277225740358531607638866809626162614242940067864245019071482791248171844982397521930582454173681491594668678670733042074255903768208195714766
n = 2200911270816846838022388357422161552282496835763864725672800875786994850585872907705630132325051034876291845289429009837283760741160188885749171857285407
b_x = int(0x7f0489e4efe6905f039476db54f9b6eac654c780342169155344abc5ac90167adc6b8dabacec643cbe420abffe9760cbc3e8a2b508d24779461c19b20e242a38)
b_y = int(0xdd04134e747354e5b9618d8cb3f60e03a74a709d4956641b234daa8a65d43df34e18d00a59c070801178d198e8905ef670118c15b0906d3a00a662d3a2736bf)
B = Point(b_x, b_y)
shared_secret_point = double_and_add(n, B, a, p)
shared_secret = shared_secret_point[0]
data = {'iv': '719700b2470525781cc844db1febd994', 'encrypted_flag': '335470f413c225b705db2e930b9d460d3947b3836059fb890b044e46cbb343f0'}
decrypted = decrypt_flag(shared_secret, data)
print("Decrypted:", decrypted.decode())