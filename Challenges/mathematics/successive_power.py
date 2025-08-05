from sympy import isprime

powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

for p in range(100, 1000):
    if not isprime(p):
        continue

    for x in range(1, p):
        valid = True 

        for i in range(len(powers) - 1):
            left = (x * powers[i]) % p
            right = powers[i + 1]
            if left != right:
                valid = False
                break  

        if valid:
            print("Prime p =", p)
            print("Base x  =", x)
            exit()
