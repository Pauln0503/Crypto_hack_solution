from pwn import remote
import json, base64, codecs, array
from Crypto.Util.number import long_to_bytes

def recv_json(sock):
    return json.loads(sock.recvline().decode())

def send_json(sock, data):
    sock.sendline(json.dumps(data).encode())

def decode_message(encoding, data):
    if encoding == 'base64':
        return base64.b64decode(data).decode()
    elif encoding == 'hex':
        return bytes.fromhex(data).decode()
    elif encoding == 'rot13':
        return codecs.decode(data, 'rot_13')
    elif encoding == 'bigint':
        return long_to_bytes(int(data, 16)).decode()
    elif encoding == 'utf-8':
        return bytes(array.array('b', data)).decode()
    else:
        raise ValueError(f"Unknown encoding type: {encoding}")

def main():
    conn = remote('socket.cryptohack.org', 13377)

    for level in range(101):
        payload = recv_json(conn)

        if 'flag' in payload:
            print(" Flag:", payload['flag'])
            break

        encoding_type = payload.get('type')
        encoded_value = payload.get('encoded')

        print(f"[{level}] Decoding {encoding_type}...")

        try:
            decoded = decode_message(encoding_type, encoded_value)
            send_json(conn, { "decoded": decoded })
        except Exception as err:
            print(f"Error decoding: {err}")
            break

if __name__ == "__main__":
    main()
