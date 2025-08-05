
def exGCD(a,b):
    if b == 0:
        return (a,1,0)
    else:
        (gcd, u1, v1) = exGCD(b, a % b)
        u = v1
        v=u1-(a//b)*v1
        return (gcd,u,v)

def main():
    p = 13
    q = 3
    gcd, u, v = exGCD(p, q)
    print(f"gcd({p},{q}) = {gcd}")
    print(f"u = {u}, v = {v}")
    print(f"Check: {p}*{u} + {q}*{v} = {p*u + q*v}")

if __name__ == "__main__":
    main()