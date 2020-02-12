import hashlib
import string
import numpy as np
import random

def sha2_256(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).digest()
    return sha_signature


class MerkleTree(object):
    
    def __init__(self,list_of_transactions):
        self.list_of_transctions = list_of_transactions

    def add(self,new_transaction):
        # Add entries to tree
        self.list_of_transctions.append(new_transaction)

    # def build():
    #     # Build tree computing new root
        

    # def get_proof(...):
    #     # Get membership proof for entry
    #     ...

    #  def get_root(...):
    #     # Return the current root
    #     ...
    
    # def verify_proof(entry, proof, root):
    #     # Verifies proof for entry and given root. Returns boolean.
    #     ...

transactions = [1]
merk = MerkleTree(transactions)
merk.add(2)
print(merk.list_of_transctions)