import numpy as np
import hashlib
import random 
import string 
import math
import json

def sha2_256(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).digest()
    return sha_signature

def myHash(n,msg):
    sha_signature = \
        hashlib.sha512(msg.encode())
    shortened_digest = (sha_signature.digest()[:n])
    return shortened_digest

x = np.random.randint(1,10)
#print(x)

list = []
next_list = []
for n in range(x):
    msg = random.choice(string.ascii_letters)   
    encoded_msg = myHash(1,msg)
    list.append(encoded_msg)

# for i in range(0,len(list),2):
#     print(i)
#     next_lvl_msg = list[i] + list[i+1]
#     encoded_next_lvl = myHash(1,next_lvl_msg)
#     next_list.append(encoded_next_lvl)

# print(list)
# print(next_list)

# y = list[0] + list[1]
# print(y)

#print(math.log(8,2))

# listoftransactions = []
# num_transactions = np.random.randint(1,10)
# print(num_transactions)
# for n in range(num_transactions):
#             #initiate transactions here 
#             #append transactions to listoftransactions
#     msg = random.choice(string.ascii_letters)   
#     listoftransactions.append(msg)
# print(listoftransactions)

k = 'b'
l = 'a'
o = k + l
ans = hashlib.sha256(o.encode()).digest()
#print(ans)

# blocks = [1,2,3,4,5,6,7,8,9,10]

# secondary = []

# for k in [blocks[x:x+2] for x in range(0, len(blocks),2)]:
#     #print(secondary)
#     secondary.append(k[0] + k[1])
# print(secondary)

# sec2 = []
# for k in range(0,len(blocks),2):
#     sec2.append(blocks[k] + blocks[k+1])
# print(sec2)

# import json 

# class Foo(object):
#     def __init__(self):
#         self.x = 1
#         self.y = 2

# foo = Foo()
# #s = json.dumps(foo) # raises TypeError with "is not JSON serializable"

# s = json.dumps(foo.__dict__) # s set to: {"x":1, "y":2}
# print(s)

class Payload(object):
    def __init__(self, action, method, data):
        self.action = action
        self.method = method
        self.data = data

import json

def as_payload(dct):
    return Payload(dct['action'], dct['method'], dct['data'])

new_Payload = Payload(1,2,3)
message = json.dumps(new_Payload.__dict__, sort_keys=True)
#print(type(message))
payload = json.loads(message, object_hook = as_payload)
#print(payload.action)


#To verify an existing signature with a public key:
import ecdsa

# SECP256k1 is the Bitcoin elliptic curve
# sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
# vk = sk.get_verifying_key()
# sig = sk.sign(b"message")
# print(vk.verify(sig, b"message")) # True


# message = b"message"
# public_key = '98cedbb266d9fc38e41a169362708e0509e06b3040a5dfff6e08196f8d9e49cebfb4f4cb12aa7ac34b19f3b29a17f4e5464873f151fd699c2524e0b7843eb383'
# sig = '740894121e1c7f33b174153a7349f6899d0a1d2730e9cc59f674921d8aef73532f63edb9c5dba4877074a937448a37c5c485e0d53419297967e95e9b1bef630d'

# vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
# print(vk.verify(bytes.fromhex(sig), message)) # True


import datetime 
print(datetime.datetime.now())
print(datetime.datetime.now().year)