from Crypto.Cipher import AES
from hashlib import sha256
import random
from itertools import product

# Load the data
with open('/Users/zukash/ghq/github.com/zukash/ctf-writeup/2025/smileyCTF/crypto/never enough/enough/out.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    given = eval(lines[0])
    ciphertext = bytes.fromhex(lines[1])

print(f"Loaded {len(given)} partial outputs")
print(f"Ciphertext: {len(ciphertext)} bytes")

def test_key_combination(lower_bits_list):
    """Test a specific combination of lower bits"""
    key_str = ""
    
    for i in range(min(len(given), len(lower_bits_list))):
        if len(key_str) >= 100:
            break
        partial = given[i]
        lower_bits = lower_bits_list[i]
        full_x = (partial << 12) | lower_bits
        key_str += str(full_x % (2**12))
    
    if len(key_str) < 100:
        return None
        
    key_str = key_str[:100]
    key = sha256(key_str.encode()).digest()
    
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
        decrypted = decrypted.rstrip(b'\x00')
        
        # Check various flag formats
        if (b'smiley{' in decrypted or b'CTF{' in decrypted or 
            b'flag{' in decrypted or b'FLAG{' in decrypted):
            return decrypted
        
        # Check if it's reasonable ASCII text
        if all(32 <= b <= 126 for b in decrypted) and len(decrypted) >= 10:
            # Additional check for flag-like patterns
            text = decrypted.decode('ascii', errors='ignore')
            if any(word in text.lower() for word in ['flag', 'ctf', 'smiley']):
                return decrypted
            
    except Exception:
        pass
    
    return None

# Smart brute force approach
print("Starting targeted brute force...")

# First, let's try some common patterns for just the first few values
# to see if we can identify a pattern

for seed in range(1000):  # Try different seeds for lower bits pattern
    if seed % 100 == 0:
        print(f"Trying seed {seed}...")
    
    # Use a simple PRNG to generate lower bits
    rng = random.Random(seed)
    lower_bits_list = [rng.randint(0, 4095) for _ in range(len(given))]
    
    result = test_key_combination(lower_bits_list)
    if result:
        print(f"Found flag with seed {seed}: {result}")
        break

# If that doesn't work, try some specific patterns
print("Trying systematic patterns...")

patterns_to_try = [
    # Pattern 1: All zeros
    [0] * len(given),
    
    # Pattern 2: Sequential
    [i % 4096 for i in range(len(given))],
    
    # Pattern 3: Reverse sequential
    [(4095 - i) % 4096 for i in range(len(given))],
    
    # Pattern 4: Powers of 2
    [(1 << (i % 12)) for i in range(len(given))],
    
    # Pattern 5: Fibonacci-like
    [((i * (i + 1)) // 2) % 4096 for i in range(len(given))],
]

for i, pattern in enumerate(patterns_to_try):
    print(f"Trying pattern {i + 1}/{len(patterns_to_try)}")
    result = test_key_combination(pattern)
    if result:
        print(f"Found flag with pattern {i + 1}: {result}")
        break

# Try some combinations based on the actual values
print("Trying value-based patterns...")

# Pattern based on the given values themselves
for multiplier in range(1, 20):
    lower_bits_list = [(given[i] * multiplier) % 4096 for i in range(len(given))]
    result = test_key_combination(lower_bits_list)
    if result:
        print(f"Found flag with multiplier {multiplier}: {result}")
        break

# Try XOR patterns
for xor_val in [0x555, 0xaaa, 0x123, 0x321, 0x777]:
    lower_bits_list = [(given[i] ^ xor_val) % 4096 for i in range(len(given))]
    result = test_key_combination(lower_bits_list)
    if result:
        print(f"Found flag with XOR {hex(xor_val)}: {result}")
        break

print("Advanced brute force complete")