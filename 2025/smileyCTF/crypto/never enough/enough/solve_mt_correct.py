from Crypto.Cipher import AES
from hashlib import sha256
import random

# Load the data
with open('/Users/zukash/ghq/github.com/zukash/ctf-writeup/2025/smileyCTF/crypto/never enough/enough/out.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    given = eval(lines[0])
    ciphertext = bytes.fromhex(lines[1])

print(f"Given: {len(given)} partial outputs")
print(f"Ciphertext: {len(ciphertext)} bytes")

# Let's understand the problem better
# The original code:
# danger = 624 * 32  # 19968
# for _ in range(danger // 20 - 16):  # 998 - 16 = 982 iterations
#     x = getrandbits(32)
#     key += str(x % 2**12)  # lower 12 bits for key
#     given.append(x >> 12)  # upper 20 bits given to us

# So we have 982 values, each representing the upper 20 bits of a 32-bit random number
# We need to recover the lower 12 bits to reconstruct the key

print(f"Need to recover lower 12 bits for {len(given)} values")
print(f"Key will be first 100 characters of concatenated str(x % 4096)")

# The key insight: Python's random.getrandbits(32) uses MT19937
# But we can try a different approach - since we know the structure,
# let's try to use the fact that the MT19937 state space is limited

def mt19937_clone_attack():
    """
    Try to clone the MT19937 state by trying different combinations
    and seeing if we can predict future values
    """
    
    # Create our own MT19937 instance
    test_rng = random.Random()
    
    # Try different seeds to see if we can match the pattern
    for seed in range(10000):
        if seed % 1000 == 0:
            print(f"Trying seed {seed}...")
            
        test_rng.seed(seed)
        
        # Generate the same sequence and compare
        matches = 0
        test_values = []
        
        for i in range(len(given)):
            x = test_rng.getrandbits(32)
            upper_20 = x >> 12
            test_values.append(upper_20)
            
            if upper_20 == given[i]:
                matches += 1
        
        # If we get a significant number of matches, this might be the right seed
        if matches > len(given) * 0.1:  # At least 10% match
            print(f"Seed {seed} has {matches} matches out of {len(given)}")
            
            if matches > len(given) * 0.9:  # 90% match - probably the right one
                print(f"Found likely seed: {seed}")
                return seed, test_rng
    
    return None, None

# Try the clone attack first
print("Attempting MT19937 clone attack...")
found_seed, found_rng = mt19937_clone_attack()

if found_seed is not None:
    print(f"Using seed {found_seed} to reconstruct key...")
    
    # Reset RNG with found seed
    found_rng.seed(found_seed)
    
    # Reconstruct the key
    key_str = ""
    for i in range(len(given)):
        x = found_rng.getrandbits(32)
        key_str += str(x % (2**12))
        
        if len(key_str) >= 100:
            break
    
    key_str = key_str[:100]
    key = sha256(key_str.encode()).digest()
    
    # Try to decrypt
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    decrypted = decrypted.rstrip(b'\x00')
    
    print(f"Decrypted: {decrypted}")
else:
    print("Clone attack failed, trying partial reconstruction...")
    
    # Alternative approach: try to find patterns in the lower bits
    # by exploiting MT19937 properties
    
    # Let's try a more systematic approach to the lower bits
    # We know that consecutive MT19937 outputs are related
    
    def try_mt_state_recovery():
        # Try to recover internal state from the partial outputs
        # This is complex, so let's try a simpler brute force on key space
        
        print("Trying optimized brute force on key combinations...")
        
        # Since we only need 100 characters of key, let's focus on first ~25 values
        # (each contributes up to 4 characters: str(x % 4096) can be 1-4 chars)
        
        key_length_so_far = 0
        values_needed = 0
        
        # Figure out how many values we need to get 100 key characters
        for i in range(len(given)):
            partial = given[i]
            # The lower 12 bits can be 0-4095, contributing 1-4 characters
            max_contribution = len(str(4095))  # 4 characters max
            key_length_so_far += max_contribution
            values_needed += 1
            
            if key_length_so_far >= 100:
                break
        
        print(f"Need to brute force lower bits for first {values_needed} values")
        
        # This is still too large (2^(12*values_needed))
        # Let's try a more targeted approach
        
        # Try common patterns for lower bits
        patterns = [
            # Pattern 1: Based on position
            lambda i: i % 4096,
            lambda i: (i * 17) % 4096,  
            lambda i: (i * i) % 4096,
            
            # Pattern 2: Based on upper bits
            lambda i: given[i] % 4096,
            lambda i: (given[i] * 13) % 4096,
            lambda i: (given[i] ^ 0x555) % 4096,
            
            # Pattern 3: Constant offsets
            lambda i: 0,
            lambda i: 1,
            lambda i: 4095,
            lambda i: 2048,
        ]
        
        for pattern_idx, pattern_func in enumerate(patterns):
            print(f"Trying pattern {pattern_idx + 1}/{len(patterns)}")
            
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
                    
                    # Check if this looks like a flag
                    if any(flag_start in decrypted for flag_start in [b'smiley{', b'CTF{', b'flag{']):
                        print(f"Found flag with pattern {pattern_idx + 1}: {decrypted}")
                        return decrypted
                    elif decrypted.startswith(b'smiley') or b'flag' in decrypted.lower():
                        print(f"Possible flag with pattern {pattern_idx + 1}: {decrypted}")
                    elif all(32 <= b <= 126 for b in decrypted) and len(decrypted) > 10:
                        print(f"Readable text with pattern {pattern_idx + 1}: {decrypted}")
                        
                except Exception as e:
                    continue
        
        return None
    
    result = try_mt_state_recovery()
    if result:
        print(f"Final result: {result}")
    else:
        print("Could not recover flag with current approaches")

print("Attack complete.")