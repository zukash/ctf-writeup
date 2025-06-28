from Crypto.Cipher import AES
from hashlib import sha256
import random

class MT19937:
    def __init__(self):
        self.mt = [0] * 624
        self.index = 0
    
    def seed(self, seed):
        self.mt[0] = seed
        for i in range(1, 624):
            self.mt[i] = (1812433253 * (self.mt[i-1] ^ (self.mt[i-1] >> 30)) + i) & 0xffffffff
        self.index = 0
    
    def extract_number(self):
        if self.index >= 624:
            self.generate_numbers()
        
        y = self.mt[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= y >> 18
        
        self.index += 1
        return y & 0xffffffff
    
    def generate_numbers(self):
        for i in range(624):
            y = (self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)
            self.mt[i] = self.mt[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.mt[i] ^= 0x9908b0df
        self.index = 0

def untemper(y):
    # Reverse the tempering operations
    y ^= y >> 18
    y ^= (y << 15) & 0xefc60000
    
    # This one is trickier
    for _ in range(7):
        y ^= (y << 7) & 0x9d2c5680
    
    y ^= y >> 11
    y ^= y >> 11  # Need to do this twice due to the shift size
    
    return y & 0xffffffff

def recover_state_from_partial_outputs(partial_outputs):
    """
    Recover MT19937 state from partial outputs where we have upper 20 bits of each output
    """
    n_outputs = len(partial_outputs)
    print(f"Trying to recover from {n_outputs} partial outputs")
    
    # We need at least 624 outputs to recover the full state
    if n_outputs < 624:
        print("Not enough outputs for full state recovery, trying brute force approach")
        return brute_force_key_recovery(partial_outputs)
    
    # Try to recover the full outputs by brute forcing the lower 12 bits
    possible_states = []
    
    # For the first approach, let's assume lower bits are 0 and see if we can get a valid state
    full_outputs = []
    for partial in partial_outputs[:624]:
        # Assume lower 12 bits are 0 for initial attempt
        full_output = partial << 12
        full_outputs.append(full_output)
    
    # Try to untemper these to get the internal state
    internal_state = []
    for output in full_outputs:
        internal_state.append(untemper(output))
    
    # Create MT instance and set the state
    mt = MT19937()
    mt.mt = internal_state[:624]
    mt.index = 624  # Force regeneration on next call
    
    # Test if this state produces outputs consistent with our known partials
    test_outputs = []
    for i in range(min(50, len(partial_outputs))):  # Test first 50
        generated = mt.extract_number()
        test_outputs.append(generated >> 12)
    
    # Check if generated outputs match our partials
    matches = sum(1 for i in range(len(test_outputs)) if test_outputs[i] == partial_outputs[i])
    print(f"Initial state guess matches: {matches}/{len(test_outputs)}")
    
    if matches > len(test_outputs) * 0.8:  # If > 80% match, probably good
        return recover_key_from_state(mt, len(partial_outputs))
    
    # If initial guess doesn't work, try more sophisticated recovery
    return brute_force_key_recovery(partial_outputs)

def recover_key_from_state(mt, num_values):
    """Recover the key using the MT19937 state"""
    # Reset the MT to generate from beginning
    mt.index = 0
    
    key_str = ""
    for i in range(num_values):
        if len(key_str) >= 100:
            break
        x = mt.extract_number()
        key_str += str(x % (2**12))
    
    key_str = key_str[:100]
    return sha256(key_str.encode()).digest()

def brute_force_key_recovery(partial_outputs):
    """Brute force approach when state recovery fails"""
    print("Using brute force approach...")
    
    # Try different patterns for the missing lower bits
    patterns = [
        lambda i: 0,  # All zeros
        lambda i: i % 4096,  # Sequential
        lambda i: (i * 17) % 4096,  # Linear congruential
        lambda i: (i * i) % 4096,  # Quadratic
        lambda i: ((i * 1103515245 + 12345) % (2**31)) % 4096,  # LCG pattern
    ]
    
    for pattern_idx, pattern in enumerate(patterns):
        print(f"Trying pattern {pattern_idx + 1}/{len(patterns)}")
        
        key_str = ""
        for i in range(min(len(partial_outputs), 200)):  # Only need enough for 100 char key
            if len(key_str) >= 100:
                break
            partial = partial_outputs[i]
            lower_bits = pattern(i)
            full_x = (partial << 12) | lower_bits
            key_str += str(full_x % (2**12))
        
        if len(key_str) >= 100:
            key_str = key_str[:100]
            key = sha256(key_str.encode()).digest()
            
            # Test this key
            result = test_key(key)
            if result:
                print(f"Success with pattern {pattern_idx + 1}!")
                return result
    
    return None

def test_key(key):
    """Test if a key successfully decrypts the ciphertext"""
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
        # Remove padding
        decrypted = decrypted.rstrip(b'\x00')
        
        # Check if it looks like a flag
        if b'smiley{' in decrypted or b'CTF{' in decrypted:
            return decrypted
        elif b'flag' in decrypted.lower():
            return decrypted
        # Check if it's printable ASCII
        elif all(32 <= b <= 126 for b in decrypted):
            if len(decrypted) > 10:  # Reasonable flag length
                return decrypted
    except Exception as e:
        pass
    
    return None

# Read the data
with open('/Users/zukash/ghq/github.com/zukash/ctf-writeup/2025/smileyCTF/crypto/never enough/enough/out.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    given = eval(lines[0])
    ciphertext = bytes.fromhex(lines[1])

print(f"Loaded {len(given)} partial outputs and {len(ciphertext)} byte ciphertext")

# Try to recover the key
result = recover_state_from_partial_outputs(given)

if result:
    print(f"Flag found: {result}")
else:
    print("Could not recover the flag")