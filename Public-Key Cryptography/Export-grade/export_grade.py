from sympy.ntheory import discrete_log

# Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0xba2432f3bc9907b4"}
# Intercepted from Bob: {"B": "0xa772c5b31c2ed9d1"}
# Intercepted from Alice: {"iv": "044bbef64b1728ba2b25bee06397d885", "encrypted_flag": "c77fbc5468843c72ff0875b1cd76e2731e758f1a61aa84f1bba221cb2e2d25da"}

p = int("0xde26ab651b92a129", 16)
g = int("0x2", 16)
A = int("0xba2432f3bc9907b4", 16)
B = int("0xa772c5b31c2ed9d1", 16)

print("A: ",A)
print("B: ",B)
print("p: ", p)

## find a
a = discrete_log(p, A, g)
print("a =", a)

## count k
K = pow(B,a,p)

print(K)