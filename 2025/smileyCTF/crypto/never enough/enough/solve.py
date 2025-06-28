from Crypto.Cipher import AES
from hashlib import sha256
import random

def untemper(y):
    y ^= y >> 18
    y ^= (y << 15) & 0xefc60000
    y ^= (y << 7) & 0x9d2c5680
    y ^= y >> 11
    return y & 0xffffffff

def mt19937_reverse(outputs):
    MT = [0] * 624
    
    # Convert partial outputs back to full 32-bit values
    for i in range(len(outputs)):
        # We have outputs[i] = (getrandbits(32) >> 12)
        # This means we have the upper 20 bits, need to find lower 12 bits
        upper_20 = outputs[i]
        
        # Try all possible lower 12 bits
        for lower_12 in range(4096):
            candidate = (upper_20 << 12) | lower_12
            
            # Test if this could be a valid MT output
            untempered = untemper(candidate)
            MT[i] = untempered
            
            # For the first candidate, we'll verify later
            if lower_12 == 0:
                break
    
    # We need 624 values to fully recover the state
    # We have fewer, so we'll use a different approach
    
    # Use the fact that we know the structure of the key generation
    given = outputs
    recovered_randoms = []
    
    # For each given value, we need to recover the original random number
    for i, partial in enumerate(given):
        # The original was: x = getrandbits(32)
        # We got: partial = x >> 12
        # And used: x % 2**12 for key
        
        # We need to find x such that x >> 12 == partial
        # This means x = (partial << 12) + (x % 4096)
        
        # We'll brute force the lower 12 bits
        best_candidate = None
        for lower_bits in range(4096):
            candidate = (partial << 12) | lower_bits
            recovered_randoms.append(candidate)
            break  # Take the first candidate for now
    
    return recovered_randoms

# Read the output
with open('/Users/zukash/ghq/github.com/zukash/ctf-writeup/2025/smileyCTF/crypto/never enough/enough/out.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    given = eval(lines[0])  # List of partial random values
    ciphertext = bytes.fromhex(lines[1])

print(f"Given {len(given)} partial values")
print(f"Ciphertext length: {len(ciphertext)} bytes")

# The vulnerability is that we need 624*32 bits but only got (624*32//20 - 16) values
# That's about 998 values, each missing 12 bits
danger = 624 * 32
num_given = danger // 20 - 16
print(f"Expected {num_given} values, got {len(given)}")

# Try to recover the key by brute forcing the missing bits
# Since we only need the first 100 characters of the key string
key_candidates = []

def try_key_recovery():
    # We need to reconstruct the key string from the first part of the generation
    key_parts = []
    
    for i in range(min(len(given), 100)):  # We only need first 100 chars
        partial = given[i]
        
        # Original: x = getrandbits(32)
        # We have: partial = x >> 12  
        # Key uses: str(x % 2**12)
        
        # So x = (partial << 12) + (x % 4096)
        # We need to find the lower 12 bits
        
        for lower_12 in range(4096):
            full_x = (partial << 12) | lower_12
            key_part = str(full_x % (2**12))
            key_parts.append(key_part)
            break  # For now, try with lower_12 = 0
    
    key_string = ''.join(key_parts)[:100]
    key = sha256(key_string.encode()).digest()
    
    # Try to decrypt
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
        # Check if it looks like a flag
        if b'smiley' in decrypted.lower() or b'flag' in decrypted.lower() or decrypted.startswith(b'smiley{'):
            return decrypted, key_string
    except:
        pass
    
    return None, None

# This approach won't work easily, let's try a different strategy
# We know the MT19937 state can be recovered with 624 consecutive outputs
# But we have partial outputs - let's implement the proper attack

def recover_mt_state_partial(partials):
    # Each partial is the upper 20 bits of a 32-bit MT output
    # We need to recover the full outputs and then untemper them
    
    mt_state = []
    
    # For MT19937 state recovery, we need the exact sequence
    # Let's try a different approach - use the known structure
    
    # Generate all possible keys and test them
    for attempt in range(1000):  # Try different combinations of lower bits
        key_str = ""
        
        for i in range(min(len(partials), 100)):
            partial = partials[i]
            # Try different lower 12 bits based on attempt number
            lower_bits = (attempt * 7 + i * 13) % 4096  # Some variation
            full_x = (partial << 12) | lower_bits
            key_str += str(full_x % (2**12))
        
        if len(key_str) >= 100:
            key_str = key_str[:100]
            key = sha256(key_str.encode()).digest()
            
            cipher = AES.new(key, AES.MODE_ECB)
            try:
                decrypted = cipher.decrypt(ciphertext)
                # Look for flag-like content
                if b'smiley{' in decrypted or b'CTF{' in decrypted:
                    print(f"Found flag: {decrypted}")
                    return decrypted
                elif all(32 <= b <= 126 for b in decrypted.rstrip(b'\x00')):
                    print(f"Readable text (attempt {attempt}): {decrypted}")
            except:
                continue
    
    return None

result = recover_mt_state_partial(given)
if not result:
    print("Could not recover the flag with simple approach")
    print("Need more sophisticated MT19937 state recovery")