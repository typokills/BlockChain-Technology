import json 
import ecdsa
from hashlib import sha512
import hashlib

def sha2_256(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).digest()
    return sha_signature

class Transaction(object):

    def __init__(self,sender_public, amt, receiver):
        # Instantiates object from passed values
        self.sender_public = sender_public
        self.amt = amt
        self.receiver = receiver
        self.signature = 'placeholder' #takes from signed 
        #self.comment = comment
        #date time stamp 

    def serialize(self):
        # Serializes object to CBOR or JSON string 
        #https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
        
        Serialized = json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4) # sort_keys is so that the keys will be sorted in alphabetical order after serializing.
        return Serialized

    def deserialize(self):

        
        return Payload(dct['action'], dct['method'], dct['data'])


    def sign(self,private_key):
    # Sign object with private key passed
    # That can be called within new()
        self.signature = private_key.sign(self.serialize().encode("utf-8"))
        print(self.serialize().encode("utf-8"))
         #might need to decode in the future 
        return self.signature

tx = Transaction(1,2,3)

#Testing Serialization
s = tx.serialize()
print(s)

#Testing Deserialization 
# x = tx.deserialize(s)
# print(x)
# print(type(x))

