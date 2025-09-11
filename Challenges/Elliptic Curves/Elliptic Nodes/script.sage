from Crypto.Util.number import long_to_bytes
p = 4368590184733545720227961182704359358435747188309319510520316493183539079703
a = 64186688762130075872648727143532923412208390610536286437268423112
b = 32579945572763798990069104934898692239152360555014084068553395172709029894

Gx, Gy = (
    8742397231329873984594235438374590234800923467289367269837473862487362482,
    225987949353410341392975247044711665782695329311463646299187580326445253608
)

Qx, Qy = (
    2582928974243465355371953056699793745022552378548418288211138499777818633265,
    2421683573446497972507172385881793260176370025964652384676141384239699096612
)

F = GF(p)
R.<x> = PolynomialRing(F)
f = x^3 + F(a)*x + F(b)

double_root = None
for r in f.roots(multiplicities=False):
    if f.derivative()(r) == 0:
        double_root = r
        break
if double_root is None:
    raise ValueError("Nah not singular")

print(f"Double root = {double_root}")

f2 = f(x + double_root)
print("Shifted curve factorization:", f2.factor())

coeffs = f2.coefficients(sparse=False)
coeff_x2 = coeffs[2] if len(coeffs) > 2 else F(0)

_Qx, _Qy = F(Qx) - double_root, F(Qy)
_Gx, _Gy = F(Gx) - double_root, F(Gy)

if coeff_x2 == 0: #cusp 
    v = (_Qy / _Qx) % p
    u = (_Gy / _Gx) % p
else: #node
    t = coeff_x2.sqrt()
    v = ((_Qy + t*_Qx) / (_Qy - t*_Qx)) % p
    u = ((_Gy + t*_Gx) / (_Gy - t*_Gx)) % p

n = discrete_log(F(v), F(u))
print("Private key is: ", n)
print(long_to_bytes(n))

