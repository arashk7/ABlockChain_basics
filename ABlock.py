import hashlib
import json


class ABlock():
    def __init__(self, timestamp, transactions_list, prev_hash=''):
        self.nonce = 0
        self.timestamp = timestamp
        self.transaction_list = transactions_list
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        block_string = json.dumps(
            {'nonce:': self.nonce, 'tstamp': str(self.timestamp), 'transaction': self.transaction_list[0].amount,
             'prevhash': self.prev_hash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != str('').zfill(difficulty):
            self.nonce += 1
            self.hash = self.calc_hash()
        print('Block mined ', self.hash)

    def __str__(self):
        string = 'nonce: ' + str(self.nonce) + '\n'
        string += 'tstamp: ' + str(self.timestamp) + '\n'
        string += 'transaction: ' + str(self.transaction_list[0]) + '\n'
        string += 'prevhash: ' + str(self.prev_hash) + '\n'
        string += 'hash: ' + str(self.hash) + '\n'
