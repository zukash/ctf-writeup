from Crypto.Cipher import AES
from hashlib import sha256
import random
# from mt19937predictor import MT19937Predictor

# Load the data
with open('/Users/zukash/ghq/github.com/zukash/ctf-writeup/2025/smileyCTF/crypto/never enough/enough/out.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    given = eval(lines[0])
    ciphertext = bytes.fromhex(lines[1])

print(f"Given: {len(given)} partial outputs")
print(f"Ciphertext: {len(ciphertext)} bytes")

def mt19937_untemper(y):
    """Untemper a MT19937 output to get internal state value"""
    y = y & 0xffffffff
    
    # Reverse the tempering operations in reverse order
    y ^= y >> 18
    y ^= (y << 15) & 0xefc60000
    
    # For this one, we need to be more careful
    for _ in range(7):  # Iterate to fully reverse
        y ^= (y << 7) & 0x9d2c5680
    
    # Reverse the first operation
    y ^= y >> 11
    y ^= y >> 11  # Do it twice for 32-bit numbers
    
    return y & 0xffffffff

def recover_mt19937_state():
    """
    Try to recover the MT19937 internal state from partial outputs
    """
    print("Attempting to recover MT19937 state from partial outputs...")
    
    # We have upper 20 bits, need to guess lower 12 bits
    # Let's try a systematic approach
    
    # For each possible combination of the first few values' lower bits,
    # see if we can reconstruct a valid MT19937 sequence
    
    max_attempts = 1000
    attempt = 0
    
    for lower_pattern in range(max_attempts):
        if attempt % 100 == 0:
            print(f"Attempt {attempt}/{max_attempts}")
        
        # Generate a pattern for lower bits based on attempt number
        lower_bits = []
        for i in range(len(given)):
            # Use different strategies for lower bits
            if lower_pattern < 100:
                # Simple patterns
                bit_val = (lower_pattern + i) % 4096
            elif lower_pattern < 200:
                # Based on upper bits
                bit_val = (given[i] * (lower_pattern - 99)) % 4096
            elif lower_pattern < 300:
                # XOR patterns
                bit_val = (given[i] ^ (lower_pattern - 199)) % 4096
            else:
                # Random-like patterns
                bit_val = ((lower_pattern * 31 + i * 17) ^ (i << 2)) % 4096
            
            lower_bits.append(bit_val)
        
        # Reconstruct full outputs
        full_outputs = []
        for i in range(len(given)):
            full_output = (given[i] << 12) | lower_bits[i]
            full_outputs.append(full_output)
        
        # Now try to see if these could be valid MT19937 outputs
        # by building the key and testing decryption
        key_str = ""
        for i in range(len(full_outputs)):
            if len(key_str) >= 100:
                break
            key_str += str(full_outputs[i] % (2**12))
        
        if len(key_str) >= 100:
            key_str = key_str[:100]
            key = sha256(key_str.encode()).digest()
            
            # Test decryption
            cipher = AES.new(key, AES.MODE_ECB)
            try:
                decrypted = cipher.decrypt(ciphertext)
                decrypted = decrypted.rstrip(b'\x00')
                
                # Check if this could be a flag
                if b'smiley{' in decrypted or b'CTF{' in decrypted:
                    print(f"Found flag! Pattern {lower_pattern}: {decrypted}")
                    return decrypted
                elif b'flag' in decrypted.lower() or decrypted.startswith(b'smiley'):
                    print(f"Possible flag with pattern {lower_pattern}: {decrypted}")
                elif all(32 <= b <= 126 for b in decrypted) and len(decrypted) >= 15:
                    print(f"Readable text with pattern {lower_pattern}: {decrypted}")
                    # If it's reasonable ASCII, it might be the flag
                    if any(word in decrypted.decode('ascii', errors='ignore').lower() 
                           for word in ['smiley', 'ctf', 'flag']):
                        print(f"Likely flag: {decrypted}")
                        return decrypted
                        
            except Exception:
                pass
        
        attempt += 1
    
    return None

# Also try some specific mathematical relationships
def try_mathematical_patterns():
    """Try patterns based on mathematical relationships"""
    print("Trying mathematical patterns...")
    
    patterns = [
        # Linear relationships
        (lambda i: (given[i] % 4096), "given[i] % 4096"),
        (lambda i: ((given[i] * 3) % 4096), "given[i] * 3 % 4096"),
        (lambda i: ((given[i] + i) % 4096), "given[i] + i % 4096"),
        (lambda i: ((given[i] ^ i) % 4096), "given[i] ^ i % 4096"),
        
        # Based on position
        (lambda i: (i % 4096), "i % 4096"),
        (lambda i: ((i * 17 + 23) % 4096), "i * 17 + 23 % 4096"),
        (lambda i: ((i * i) % 4096), "i^2 % 4096"),
        
        # Constants
        (lambda i: 0, "all zeros"),
        (lambda i: 1, "all ones"),
        (lambda i: 4095, "all max"),
        
        # Bit patterns
        (lambda i: (0x555 if i % 2 == 0 else 0xaaa), "alternating bit pattern"),
    ]
    
    for pattern_func, pattern_name in patterns:
        print(f"Trying pattern: {pattern_name}")
        
        key_str = ""
        for i in range(len(given)):
            if len(key_str) >= 100:
                break
            
            partial = given[i]
            lower_bits = pattern_func(i)
            full_x = (partial << 12) | lower_bits
            key_str += str(full_x % (2**12))
        
        if len(key_str) >= 100:
            key_str = key_str[:100]
            key = sha256(key_str.encode()).digest()
            
            cipher = AES.new(key, AES.MODE_ECB)
            try:
                decrypted = cipher.decrypt(ciphertext)
                decrypted = decrypted.rstrip(b'\x00')
                
                print(f"  Result: {decrypted}")
                
                if (b'smiley{' in decrypted or b'CTF{' in decrypted or 
                    b'flag{' in decrypted):
                    print(f"Found flag with {pattern_name}: {decrypted}")
                    return decrypted
                elif all(32 <= b <= 126 for b in decrypted) and len(decrypted) >= 10:
                    text = decrypted.decode('ascii', errors='ignore').lower()
                    if any(word in text for word in ['smiley', 'ctf', 'flag']):
                        print(f"Likely flag with {pattern_name}: {decrypted}")
                        return decrypted
                        
            except Exception as e:
                print(f"  Decryption failed: {e}")
    
    return None

# Try both approaches
result = try_mathematical_patterns()
if not result:
    result = recover_mt19937_state()

if result:
    print(f"\nFinal flag: {result}")
else:
    print("\nCould not recover flag with any approach")