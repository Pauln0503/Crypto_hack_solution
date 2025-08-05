from pwn import remote
from Crypto.Cipher import AES
from Crypto.Hash import SHA1
import json

r = remote("socket.cryptohack.org", 13371)

r.recvline()
r.sendline(json.dumps({"p":"0x123","g":"0x123","A":"0x123"}).encode())
r.recvline()

r.sendline(json.dumps({"B":"0x1"}).encode())

r.recvuntil(b"from Alice: ")
d = json.loads(r.recvline())
iv = bytes.fromhex(d["iv"])
ct = bytes.fromhex(d["encrypted_flag"])


k = SHA1.new(b'1').digest()[:16]
m = AES.new(k, AES.MODE_CBC, iv).decrypt(ct)


print(m.decode())