
import requests
import time
import string

class ECBOracle:
    def __init__(self, base_url="http://aes.cryptohack.org/ecb_oracle/encrypt/"):
        self.base_url = base_url
    
    def get_ciphertext(self, data):
        """Send payload to encryption oracle and return ciphertext"""
        response = requests.get(self.base_url + data + '/')
        return response.json()['ciphertext']

def display_blocks(hex_string, block_size):
    """Display hex string in blocks of specified size"""
    for idx in range(0, len(hex_string), block_size):
        print(hex_string[idx:idx+block_size], ' ', end='')
    print()

def extract_secret():
    """Extract the secret flag using ECB oracle attack"""
    oracle = ECBOracle()
    discovered_flag = ''
    padding_length = 31  # 32 - 1
    
    # Character set for brute force
    charset = '_@}{' + string.digits + string.ascii_lowercase + string.ascii_uppercase
    
    while True:
        # Create padding to align blocks
        padding = '1' * (padding_length - len(discovered_flag))
        
        # Get target ciphertext
        target_cipher = oracle.get_ciphertext(padding.encode().hex())
        print('Target:', end=' ')
        display_blocks(target_cipher, 32)
        
        # Try each character
        for candidate_char in charset:
            test_input = padding + discovered_flag + candidate_char
            test_cipher = oracle.get_ciphertext(test_input.encode().hex())
            
            print(f'{candidate_char}:', end=' ')
            display_blocks(test_cipher, 32)
            
            # Compare second block (indices 32:64)
            if test_cipher[32:64] == target_cipher[32:64]:
                discovered_flag += candidate_char
                print(f"Found: {discovered_flag}")
                break
            
            time.sleep(1)
        
        # Check if we've found the complete flag
        if discovered_flag.endswith('}'):
            break
    
    print(f"Complete flag: {discovered_flag}")
    return discovered_flag

if __name__ == "__main__":
    extract_secret()
