import hashlib

def sha2_256(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).digest()
    return sha_signature

y1 = sha2_256("Blockchain Technology")
#print("sha2_256: ",y1)

def sha2_512(hash_string):
    sha_signature = \
        hashlib.sha512(hash_string.encode())
    return sha_signature

y256 = sha2_512("Blockchain Technology")
#print("sha2_512: ",y256.digest())

def sha3_256(hash_string):
    sha_signature = \
        hashlib.sha3_256(hash_string.encode())
    return sha_signature

y3_256 = sha3_256("Blockchain Technology")
#print("sha3_256: ", y3_256.digest())

def sha3_512(hash_string):
    sha_signature = \
        hashlib.sha3_512(hash_string.encode())
    return sha_signature

y3_512 = sha3_512("Blockchain Technology")
print("sha3_512: ", y3_512.digest())






