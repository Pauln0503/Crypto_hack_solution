from Crypto.Util.number import inverse

def point_addition(P, Q, a, p):
    if P == "O":
        return Q
    if Q == 'O':
        return P
    
    x1,y1 = P
    x2,y2 = Q

    if x1 == x2  and (y1 + y2) % p == 0:
        return "O"
    if P != Q:
        lmbd = (y2 - y1) * inverse(x2 - x1, p) % p
    else:
        lmbd = (3 * x1**2 + a) * inverse(2 * y1, p) % p

    x3 = (lmbd**2 - x1 - x2) % p
    y3 = (lmbd * (x1 - x3) - y1) % p

    return (x3, y3)

a = 497
p = 9739
P = (493,5564)
Q=(1539,4742)
R=(4403,5202)

PP = point_addition(P, P, a, p)
PPQ = point_addition(PP, Q, a, p)
result = point_addition(PPQ, R, a, p)

print(f"Crypto{{{result[0]},{result[1]}}}")
