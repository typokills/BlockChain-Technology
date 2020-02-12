import hashlib

def myHash(n,msg):
    sha_signature = \
        hashlib.sha512(msg.encode())
    shortened_digest = (sha_signature.digest()[:n])
    return shortened_digest
for n in range(1,6):
    digest = myHash(n,'Block')
    #print(digest)

import random
import string
def randomString(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
m2 = randomString(5)
#print(m2)
#print(myHash(1,m2))

import datetime
def preimage_finder(hash_string):
    t0 = datetime.datetime.now()
    match = False
    #print(t0)
    m1 = hash_string
    #print(m1)
    while match == False:
        m2 = randomString(5)
        m2_e = myHash(2,m2)
        #print(m2_e)
        if m2_e == m1:
            match = True
    #print("m1: ",m1)
    #print("m2e: ", m2_e)
    #print('m2: ', m2)
    t1 = datetime.datetime.now()
    time_taken = t1-t0
    #print("Time Taken for pre-image:", time_taken)
preimage_finder(b"\x00"*2)

def collision_finder(n):
    collision = False
    dic = {}
    t0 = datetime.datetime.now()
    print(t0)
    while collision == False:
        m1 = randomString(5)
        key = myHash(n,m1)
        #print(m1)
        print(key)
        if key in dic:
            collision = True
        else:
            dic[key] = m1
            
    print(m1)
    print(key)
    t1 = datetime.datetime.now()
    print(t1)
    time_taken = t1-t0
    print(time_taken)