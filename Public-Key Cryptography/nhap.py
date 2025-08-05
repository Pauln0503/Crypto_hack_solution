from Crypto.Util.number import inverse
from Crypto.Util.number import bytes_to_long, long_to_bytes



n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273


p = 848445505077945374527983649411 
q = 1160939713152385063689030212503

phi = (p - 1) * (q -1 )


d = inverse(e, phi)

print(f"Private key d = {d}")

msg = pow(ct, d, n)

print(f"msg (int) = {msg}")
try:
    print("msg (ascii) =", long_to_bytes(msg).decode())
except:
    print("nah")









