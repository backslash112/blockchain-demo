class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Create a new bloc and add it to the chain
        pass

    def new_transaction(self):
        # Add a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hash a block
        pass
        
    @property
    def last_block(self):
        # Return the last block in the chain
        pass
