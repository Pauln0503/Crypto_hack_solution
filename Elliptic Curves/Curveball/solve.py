## using ECDSA generator substitution attack

from fastecdsa.curve import P256
from Crypto.Util.number import inverse
from fastecdsa.point import Point
from pwn import remote
import json

r = remote('socket.cryptohack.org', 13382)

line = r.recvline().strip()
if line.startswith(b'{') and line.endswith(b'}'):
    msg = json.loads(line.decode())
else:
    print("[*] Server:", line.decode())

# setup params
d = 2
q = P256.q
Q_bing = Point(
    0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531,
    0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A,
    curve=P256
)

fake_G = inverse(d, q) * Q_bing
assert fake_G * d == Q_bing

payload = {
    "private_key": d,
    "host": "www.bing.com",
    "curve": "P-256",
    "generator": [fake_G.x, fake_G.y]
}
r.sendline(json.dumps(payload).encode())


line = r.recvline().strip()
if line.startswith(b'{') and line.endswith(b'}'):
    resp = json.loads(line.decode())
    print("[+] Response:", resp)
else:
    print("[*] Server:", line.decode())

r.close()
