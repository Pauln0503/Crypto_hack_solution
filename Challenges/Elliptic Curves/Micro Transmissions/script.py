import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from sage.all import EllipticCurve, GF, crt, factor, Integer

def ecdlp(A, G, order, max_value_n=2**64-1):
    results = []
    factors_list = []
    mul = 1

    print("Pohlig–Hellman...ehehe")

    for prime, exponent in factor(order):
        subgroup_order = prime**exponent
        e = order // subgroup_order

        G_new = G * e
        A_new = A * e

        try:
            dlog = A_new.log(G_new)
            print(f"    - modulo {subgroup_order}: dlog = {dlog}")
        except Exception as ex:
            print(f"    - modulo {subgroup_order}: fail ({ex})")
            return None

        results.append(dlog)
        factors_list.append(subgroup_order)

        mul *= prime
        if mul > max_value_n:
            print("stop stop stop")
            break

    if results and factors_list:
        n = crt(results, factors_list)
        print("Success")
        return n

    return None

p = 99061670249353652702595159229088680425828208953931838069069584252923270946291
a, b = 1, 4
E = EllipticCurve(GF(p), [a, b])

G = E(
    43190960452218023575787899214023014938926631792651638044680168600989609069200,
    20971936269255296908588589778128791635639992476076894152303569022736123671173
)
# Find from A = E.lift_x(ax)
A = E(
    87360200456784002948566700858113190957688355783112995047798140117594305287669,
    59593466123013446762504853712989655201116629740011953821167160210569255093793
)

bx = 6082896373499126624029343293750138460137531774473450341235217699497602895121

order = G.order()
print("Order of G:", order)

n = ecdlp(A, G, order)
print("Private key n for u and me ", n)



B = E.lift_x(bx)  
shared_secret = (n * B).xy()[0]
print("Shared secret bro ", shared_secret)

data = {
    'iv': 'ceb34a8c174d77136455971f08641cc5',
    'encrypted_flag': 'b503bf04df71cfbd3f464aec2083e9b79c825803a4d4a43697889ad29eb75453'
}

def decrypt_flag(shared_secret: int, data: dict):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    iv = bytes.fromhex(data['iv'])
    ciphertext = bytes.fromhex(data['encrypted_flag'])

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    try:
        plaintext = unpad(plaintext, 16)
        return plaintext.decode('ascii')
    except ValueError:
        print("Wrongg :((")
        return plaintext
    except UnicodeDecodeError:
        print("Unicode error =))")
        return plaintext


decrypted = decrypt_flag(shared_secret, data)
print("Decrypted flag:", decrypted)
