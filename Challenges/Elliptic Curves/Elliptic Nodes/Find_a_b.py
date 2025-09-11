
from Crypto.Util.number import inverse
from collections import namedtuple

p = 4368590184733545720227961182704359358435747188309319510520316493183539079703
Gx = 8742397231329873984594235438374590234800923467289367269837473862487362482
Gy = 225987949353410341392975247044711665782695329311463646299187580326445253608
Qx = 2582928974243465355371953056699793745022552378548418288211138499777818633265  
Qy = 2421683573446497972507172385881793260176370025964652384676141384239699096612  

Point = namedtuple("Point", "x y")
O = 'Origin'
G = Point(Gx, Gy)
Q = Point(Qx, Qy)

def solve_a_b(p, P1, P2):
    x1,y1 = P1.x, P1.y
    x2,y2 = P2.x, P2.y
    A1 = (y1*y1 - (x1**3)) % p
    A2 = (y2*y2 - (x2**3)) % p
    if x1 % p == x2 % p:
        raise ValueError("x1 == x2 mod p, can't solve uniquely")
    a = ((A1 - A2) * inverse((x1 - x2) % p, p)) % p
    b = (A1 - a * x1) % p
    return a, b

a, b = solve_a_b(p, G, Q)
print("Recovered a =", a)
print("Recovered b =", b)



