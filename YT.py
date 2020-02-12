import hashlib

class MerkelTreeHash(object):
    def __init__(self):
        pass

    def find_merkel_hash(self, file_hashes):
        blocks = []

        for m in sorted(file_hashes):
            blocks.append(m)

        list_len = len(blocks)

        while list_len % 2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)

        secondary = []

        for k in [blocks[x:x+2] for x in range(0, len(blocks),2)]:
            hasher = hashlib.sha256()
            hasher.update(k[0])
            hasher.update(k[1])
            secondary.append(hasher.hexdigest())

        if len(secondary) == 1:
            return secondary[0][0:64]
        else:
            return self.find_merkel_hash(secondary)

if __name__ == '__main__':

    import uuid
    import numpy as np
    import hashlib
    import random 
    import string 
    import math
    def myHash(n,msg):
        sha_signature = \
            hashlib.sha512(msg.encode())
        shortened_digest = (sha_signature.digest()[:n])
        return shortened_digest

    file_hashes = []

    for i in range(0,13):
        msg = random.choice(string.ascii_letters)   
        encoded_msg = myHash(1,msg)
        file_hashes.append(encoded_msg)

    print1  = 'Finding the merkel tree hash of {0} random hashes'
    print (print1.format(len(file_hashes)))

    cls = MerkelTreeHash()
    mk = cls.find_merkel_hash(file_hashes)
    print ('....')
    print (file_hashes)



