from pwn import remote
import json
import hashlib
from Crypto.Util.number import bytes_to_long
from ecdsa.ecdsa import generator_192, Signature, Public_key

G = generator_192
n = G.order()

def sha1( data):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(data)
        return bytes_to_long(sha1_hash.digest())

r = remote('socket.cryptohack.org', 13381)

line = r.recvline().strip()
if line.startswith(b'{') and line.endswith(b'}'):
    msg = json.loads(line.decode)
else: 
    print ("[*] Server: ", line.decode())

# ask server for a msg sir
f_msg = {"option" : "sign_time"}
r.sendline(json.dumps(f_msg).encode())
f_resp = json.loads(r.recvline().decode())
print("[+] Response: ", f_resp)

msg = f_resp["msg"]
r_val = int(f_resp["r"], 16)
s_val = int(f_resp["s"], 16)
hm = sha1(msg.encode())

print(f"msg = {msg}")
print(f"H(m) = {hm}")
print(f"r = {r_val}, s = {s_val}")

### bruteforce private_key d
for k in range(1, 60):
    num = (s_val * k - hm) % n
    den = pow(r_val, -1, n)  # modular inverse
    d = (num * den) % n
     
    Q = G * d
    public_key = Public_key(G, Q)
    sig = Signature(r_val, s_val)
    if public_key.verifies(hm, sig):
        print(" Hello private keyyyyy: ", d)
        priv_d = d
        break
else:
     print("Nahhhhhh")
     exit()

target_msg = 'unlock'
hm2 = sha1(target_msg.encode())
k = 1  
r_point =G * k
r_for = r_point.x() % n
s_for = (pow(k, -1, n) * (hm2 + r_for * priv_d)) % n

payload = {
    "option": "verify",
    "msg": target_msg,
    "r": hex(r_for),
    "s": hex(s_for),
}
r.sendline(json.dumps(payload).encode())
print(r.recvline().decode())


