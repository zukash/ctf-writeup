import os
from Crypto.Cipher import AES
import signal

signal.alarm(3600)  # Set an alarm for 3600 seconds (1 hour) to interrupt the program

# q = 16  # Define a variable q with the value 16
q = 4  # Define a variable q with the value 16
vsize = 1  # Define a variable vsize with the value 22
o1 = 1  # Define a variable o1 with the value 22
o2 = 1  # Define a variable o2 with the value 22
m = o1 + o2  # Define m as the sum of o1 and o2
n = vsize + o1 + o2  # Define n as the sum of vsize, o1, and o2
K = GF(q)  # Define a finite field K of order q
print(f"{q = }")
print(f"{vsize = }")
print(f"{o1 = }")
print(f"{o2 = }")
print(f"{m = }")
print(f"{n = }")
print(f"{K = }")


# Create a dictionary to map polynomials to integers in the finite field
poly2int = {}
for i in range(q):
    poly2int[K(Integer(i).digits(2))] = i


# r: random_element()
# e.g. size1 = 4, size2 = 6
#
#   size2
#   vvvvvv
#  [rrrrrr000] < size1
#  [0rrrrr000] < size1
#  [00rrrr000] < size1
#  [000rrr000] < size1
#  [000000000]
#  [000000000]
#  [000000000]
#  [000000000]
#  [000000000]
# Function to create a special upper diagonal matrix
def make_UD_matrix(size1, size2):
    res = Matrix(K, n, n)  # Create an n x n matrix over the field K
    small_size = min(size1, size2)  # Determine the smaller of the two sizes
    big_size = max(size1, size2)  # Determine the larger of the two sizes

    # Fill the matrix with random elements from K in an upper diagonal pattern
    for i in range(small_size):
        for j in range(big_size):
            if i <= j:
                # res[i, j] = K.random_element()
                res[i, j] = 1
    return res


# Function to multiply a matrix with a vector
def product(mat, vec):
    res = []
    for i in range(mat.nrows()):
        element = Matrix(K, n, n)
        for j in range(mat.ncols()):
            element += mat[i, j] * vec[j]
        res.append(element)
    return res


S = random_matrix(K, n, n)
T = random_vector(K, n)
print(f"{S = }")
print(f"{T = }")
element = Matrix(K, n, n)
print(f"{S[0, 0] * T[0] = }")
element += S[0, 0] * T[0]
print(f"{element = }")
print(f"{product(S, T) = }")
print("====================")


# Function to generate a public and private key
def gen_key():
    # Generate random invertible matrices S and T
    S = random_matrix(K, n, n)
    T = random_matrix(K, m, m)
    while not S.is_invertible():
        S = random_matrix(K, n, n)
    while not T.is_invertible():
        T = random_matrix(K, m, m)

    # Create a list of special matrices
    Fs = []
    for _ in range(o1):
        Fs.append(make_UD_matrix(vsize, vsize + o1))
    for _ in range(o2):
        Fs.append(make_UD_matrix(n, vsize + o1))

    # Multiply each matrix in Fs by S and its transpose
    SFSs = []
    for F in Fs:
        SFSs.append(S * F * S.transpose())
    pubkey = SFSs
    pubkey = product(T, SFSs)

    return (pubkey, (S, T, Fs))


# Function to evaluate a vector with the public key matrices
def eval_v(pubkey, v):
    return vector([v * matp * v for matp in pubkey])


# Function to convert a vector to a string representation
def vec2string(vec):
    res = ""
    for e in vec:
        res += str(poly2int[e]) + ","
    return res[:-1]


# Function to convert a matrix to a list of string representations
def mat2strings(mat):
    res = []
    for row in mat:
        res.append(vec2string(row))
    return res


# Function to convert a string representation back to a vector
def strings2vec(str):
    res = []
    vals = str.split(",")
    for val in vals:
        res.append(K(Integer(int(val)).digits(2)))
    return vector(K, res)


# Function to convert a list of string representations back to a matrix
def strings2mat(strs, nrows, ncols):
    mat = []
    for row in strs:
        mat.append(strings2vec(row))
        assert ncols == len(mat[-1])
    assert nrows == len(mat)
    return matrix(K, mat)


# Main part of the program
message = random_vector(K, n)  # Generate a random message vector
pubkey, privkey = gen_key()  # Generate a public and private key

print(len(message))
# for challenge_id in range(2):
#     pubkey, privkey = gen_key()  # Generate a public and private key
#     ciphertext = eval_v(pubkey, message)  # Encrypt the message

#     # Convert the public key to string representation and print it
#     pubkey_str = []
#     for i in range(len(pubkey)):
#         pubkey_str.append(mat2strings(pubkey[i]))
#         print(f"pubkey[{i}]: {pubkey_str[i]}")

#     # Collect vectors from user input and check if they form a subspace
#     vecs = []
#     for i in range(22):
#         vecs.append(strings2vec(input(f"vec{i}:")))
#     V = VectorSpace(K, n)
#     S = V.subspace(vecs)
#     assert S.dimension() == 22  # Ensure the subspace has dimension 22
#     vec = S.random_element()  # Choose a random element from the subspace

#     # Print the evaluation of the random vector and the difference with the message
#     print("eval(vec) result:", vec2string(eval_v(pubkey, vec)))
#     print(
#         "eval(message+vec)-eval(message) result:",
#         vec2string(eval_v(pubkey, vec + message) - eval_v(pubkey, message)),
#     )

# Check if the user's answer matches the original message
answer = strings2vec(input("ans:"))
if answer == message:
    flag = os.getenv(
        "FLAG", "SECCON{dummyflagdummyflagdummyf}"
    )  # Get the flag from an environment variable
    print("flag:", flag)
else:
    print("flag:", "fail")  # Print failure message if the answer is incorrect
