import requests

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

r = requests.get("https://aes.cryptohack.org/bean_counter/encrypt")
ciphertext = r.json()['encrypted']

cipher_hex = ciphertext
cipher_bytes = bytes.fromhex(cipher_hex)

blocks = [cipher_bytes[i:i+16] for i in range(0, len(cipher_bytes), 16)]

png_header = bytes.fromhex("89504e470d0a1a0a0000000d49484452")

keystream = xor_bytes(blocks[0], png_header)

decrypted = b''.join([xor_bytes(block, keystream) for block in blocks])

with open("recovered_flag.png", "wb") as f:
    f.write(decrypted)