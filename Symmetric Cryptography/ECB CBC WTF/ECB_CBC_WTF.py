import httpx
from pwn import xor


BASE_URL = "http://aes.cryptohack.org/ecbcbcwtf"


def fetch_ciphertext() -> str:
    url = f"{BASE_URL}/encrypt_flag/"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()["ciphertext"]


def decrypt_ecb_block(ciphertext_hex: str) -> bytes:
    url = f"{BASE_URL}/decrypt/{ciphertext_hex}/"
    response = httpx.get(url)
    response.raise_for_status()
    pt_hex = response.json()["plaintext"]
    return bytes.fromhex(pt_hex)


def decrypt_flag(ciphertext_hex: str) -> str:
    iv = bytes.fromhex(ciphertext_hex[:32])
    ct_blocks = [ciphertext_hex[32:64], ciphertext_hex[64:]]  # 2 next block

    pt_blocks = [decrypt_ecb_block(block) for block in ct_blocks]

    pt1 = xor(iv, pt_blocks[0]).decode()
    pt2 = xor(bytes.fromhex(ct_blocks[0]), pt_blocks[1]).decode()

    return pt1 + pt2


if __name__ == "__main__":
    ciphertext = fetch_ciphertext()
    flag = decrypt_flag(ciphertext)
    print(f"Flag: {flag}")
