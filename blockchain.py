import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, proof, previous_hash=None):
        """Create a new bloc and add it to the chain

        Args:
        proof: The proof given by the proof of work algorithm
        previous_hash: (Optional) Hash of previous block

        Returns:
        New block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Reset the current list of transactions
        self.current_transactions = []
        return block

    def new_transaction(self, sender, recipient, amount):
        """Create a new transaction to go into the next mined block

        Args:
        sender: Address of the sender
        recipient: Address of the recipient
        amount: amount

        Returns:
        Return the index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Create a SHA-256 hash of a block

        Args:
        block: block
        return: hash value
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple proof of work algorithm:
        Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        p is the previous proof, and p' is the new proof

        Args:
        last_proof

        Returns:
        proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validate the proof, does hash(last_proof, proof) contains 4 leading zeroes?

        Args:
        last_proof: previous proof
        proof: current proof

        Returns:
        True if correct
        """
        guess = f'{last_proof}{proof}'.encode()
        guss_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'
