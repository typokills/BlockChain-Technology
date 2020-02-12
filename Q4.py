import json 
import ecdsa
from hashlib import sha512
import hashlib

def sha2_256(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).digest()
    return sha_signature

class Transaction(object):

    def __init__(self,sender_public, amt, receiver, comment):
        # Instantiates object from passed values
        self.sender_public = sender_public
        self.amt = amt
        self.receiver = receiver
        self.signature = 'placeholder' #takes from signed 
        self.comment = comment
        #date time stamp 
        

    def serialize(self):
        # Serializes object to CBOR or JSON string 
        #https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
        
        Serialized = json.dumps([str(i) for i in self.__dict__.values()], sort_keys = True)
     # sort_keys is so that the keys will be sorted in alphabetical order after serializing.
        return Serialized

    def as_payload(cls,dct):
        sender_public = dct['sender_public']
        amt = dct['amt'] 
        receiver = dct['receiver']
        comment = dct['comment']
        new_transaction = Transaction(sender_public, amt, receiver, comment)
        return new_transaction

    def deserialize(self,strings):
        # Instantiates/Deserializes object from CBOR or JSON string

        deserialized = json.loads(strings, object_hook = self.as_payload)
        return (deserialized)

    def sign(self,private_key):
    # Sign object with private key passed
    # That can be called within new()
        self.signature = private_key.sign(self.serialize().encode('utf-8'))
        print(self.serialize().encode("utf-8"))
         #might need to decode in the future 
        return self.signature

    def validate(self): #pass in public key
        # Validate transaction correctness.
        # Can be called within from_json()
        # verify attributes are correct 
        #issue as signed would have a different value if you used sign first
        checking_sig = self.signature
        self.signature = 'placeholder'
        s = self.serialize().encode("utf-8")
        print(type(s))
        flag = self.sender_public.verify(checking_sig,s) #self.sender_publickey.verify
        return flag

    @classmethod
    def __eq__(cls, self, transaction2):
        # Check whether transactions are the same
        flag = False
        if self.serialize() == transaction2.serialize():
            flag = True
        return flag

#check the hash of the transaction object 
private_key = ecdsa.SigningKey.generate() 
public_key = private_key.get_verifying_key()

# Testcase for .serialize 

# json_object = tx.serialize()
# print(json_object)
# print('serialize ok')

# Testcase for __eq__

eq1 = Transaction(1,2,3,4)
eq2 = Transaction('a','b','c','d')
eq3 = Transaction(1,2,3,4)

json1 = eq1.serialize()
json2 = eq2.serialize()
json3 = eq3.serialize() # or you can hash it

#print(tx.__eq__(eq1,eq3))

# Test for from_json
# print(type(json1))
# print(tx.from_json(json1))


# Testing for .signed



x = 'a'

tx = Transaction(public_key,2,3,4)


tx.sign(private_key)
print(tx.validate())

 #https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given




