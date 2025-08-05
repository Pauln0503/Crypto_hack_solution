
A = 486662
p = 2**255 - 19
x1 = 9  
k = 0x1337c0decafe

a24 = (A + 2) * pow(4, -1, p) % p

def montgomery_ladder(k, x1):
    X1 = x1
    X2, Z2 = 1, 0            
    X3, Z3 = x1, 1           
    swap = 0

    k_bits = bin(k)[2:].zfill(255)

    for i in range(len(k_bits)):
        k_i = int(k_bits[i])
        swap ^= k_i
        if swap:
            X2, X3 = X3, X2
            Z2, Z3 = Z3, Z2
        swap = k_i

        A = (X2 + Z2) % p
        AA = A * A % p
        B = (X2 - Z2) % p
        BB = B * B % p
        E = (AA - BB) % p
        C = (X3 + Z3) % p
        D = (X3 - Z3) % p
        DA = D * A % p
        CB = C * B % p
        X5 = (DA + CB) % p
        X5 = X5 * X5 % p
        Z5 = (DA - CB) % p
        Z5 = Z5 * Z5 % p
        Z5 = Z5 * X1 % p
        X4 = AA * BB % p
        Z4 = E * ((a24 * E) % p + BB) % p

        X2, Z2 = X4, Z4
        X3, Z3 = X5, Z5

    if swap:
        X2, X3 = X3, X2
        Z2, Z3 = Z3, Z2

    zinv = pow(Z2, -1, p)
    x = X2 * zinv % p
    return x

result_x = montgomery_ladder(k, x1)
print("x-coordinate of [k]G:", result_x)
