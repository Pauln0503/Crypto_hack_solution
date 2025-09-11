from pwn import remote
import json, hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

r = remote('socket.cryptohack.org', 13373)
r.recvuntil(b'Intercepted from Alice: ')
alice_data = json.loads(r.recvline())
p, g, A = alice_data['p'], alice_data['g'], alice_data['A']

r.recvuntil(b'Intercepted from Bob: ')
B = int(json.loads(r.recvline())['B'], 16)

r.recvuntil(b'Intercepted from Alice: ')
msg = json.loads(r.recvline())
iv, enc = bytes.fromhex(msg['iv']), bytes.fromhex(msg['encrypted'])

payload = {"p": p, "g": A, "A": "0x1"}
r.recvuntil(b'Bob connects to you, send him some parameters: ')
r.sendline(json.dumps(payload))

r.recvuntil(b'Bob says to you: ')
shared_secret = int(json.loads(r.recvline())['B'], 16)

key = hashlib.sha1(str(shared_secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(enc)

def decode_safe(data):
    try:
        return unpad(data, 16).decode('utf-8')
    except ValueError:
        return data

print("Decrypted message:", decode_safe(pt))
