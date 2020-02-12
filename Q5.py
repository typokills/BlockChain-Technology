import hashlib
import string
import numpy as np
import random

def sha2_256(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).digest()
    return sha_signature

class MerkleTree():

    listoftransactions = []
    
    root = 'a'
    
    def add(self,listoftransactions):
        # Add entries to tree
        num_transactions = np.random.randint(1,10)
        for n in range(num_transactions):
            #initiate transactions here 
            #append transactions to listoftransactions
            msg = random.choice(string.ascii_letters)   
            listoftransactions.append(msg)
        print('listoftransactions: ' , listoftransactions)
        
    def build(listoftransactions):
        # Build tree computing new root
        # Check if total number of transactions is divisible by 2 if not add one more
        list_len = len(listoftransactions)
        while list_len % 2 != 0:
            listoftransactions.extend(listoftransactions[-1:]) 
            
        #Secondary list used to store the new hashed keys
        secondary = []
        
        # Iterate through the whole list and pair up, encode and hash and append       
        for k in range(0, len(listoftransactions), 2):
            secondary.append(listoftransactions[k] + listoftransactions[k+1])

        if len(secondary) == 1:
            root = secondary[0]
            return root

        else:
            return self.build(secondary)
    

    def get_proof(checking_array):
        # Get membership proof for entry
        array_length = len(checking_array)
        ans_list = []

        for n in range(array_length):
            for num_hash in range(n):
                new_digest = checking_array[n]

    def get_root(self):
        # Return the current root
        return self.root

# def verify_proof(entry, proof, root):
#     # Verify the proof for the entry and given root. Returns boolean.
#     ...

new_tree = MerkleTree()
transaction_list = []
new_tree.add(transaction_list)


