from Crypto.Util.Padding import pad
import requests

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


r = requests.get("https://aes.cryptohack.org/flipping_cookie/get_cookie/")
cookie_hex = r.json()["cookie"]


cookie_bytes = bytes.fromhex(cookie_hex)
iv = cookie_bytes[:16]
cipher = cookie_bytes[16:]


orig = b"admin=False;ex"  # 13 bytes
target = b"admin=True;ex"  # same length

# Pad to 16 bytes 
orig = pad(orig, 16)
target = pad(target, 16)

# Flippin
new_iv = xor_bytes(xor_bytes(iv, orig, ), target)
print(new_iv)

r = requests.get(f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cipher.hex()}/{new_iv.hex()}/")
print(r.json())
