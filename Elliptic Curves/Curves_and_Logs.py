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

Q_a = (815,3190)
n_b = 1829

S = double_and_add(n_b, Q_a, 497, 9739)

x = S[0]
x_str = str(x)
sha1 = hashlib.sha1(x_str.encode()).hexdigest()

print(f"Crypto{{{sha1}}}")

