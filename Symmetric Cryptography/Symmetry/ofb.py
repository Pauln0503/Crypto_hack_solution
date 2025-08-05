import requests

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

r = requests.get("https://aes.cryptohack.org/symmetry/encrypt_flag/")
ciphertext = r.json()["ciphertext"]

iv_hex = ciphertext[:32]                     
#iv = bytes.fromhex(iv_hex)
cipher = bytes.fromhex(ciphertext[32:])

fake_pt = b"A" * len(cipher)

r2 = requests.get(f"https://aes.cryptohack.org/symmetry/encrypt/{fake_pt.hex()}/{iv_hex}/")

cipher_known = bytes.fromhex(r2.json()["ciphertext"])

keystream = xor_bytes(cipher_known, fake_pt)

flag = xor_bytes(cipher, keystream)
print("FLAG:", flag.decode())
