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

x_a = 4726
p = 9739
a = 497
b = 1768
n_b = 6534

rhs = (x_a**3 + a * x_a + b) % p
y_a = pow(rhs, (p + 1) // 4, p)

Q_a = (x_a, y_a)

S = double_and_add(n_b, Q_a, a, p)

print(S[0])