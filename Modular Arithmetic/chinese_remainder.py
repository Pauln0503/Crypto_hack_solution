def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No inverse exists for {a} mod {m}")
    return x % m

def chinese_remainder(a_list, n_list):
    assert len(a_list) == len(n_list)
    N = 1
    for n in n_list:
        N *= n
    
    x = 0
    for ai, ni in zip(a_list, n_list):
        Ni = N // ni
        Mi = modinv(Ni, ni)
        x += ai * Mi * Ni
    
    return x % N
