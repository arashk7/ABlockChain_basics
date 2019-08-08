from datetime import datetime
from ABlockChain_basics import ABlock, ATransaction


class ABlockChain():
    def __init__(self):
        self.chain = [self.generate_genesis_block(), ]
        self.pending_transactions = []
        self.mining_reward = 100
        self.difficulty = 4

    def generate_genesis_block(self):
        return ABlock.ABlock(datetime.now(), [ATransaction.ATransaction(None, None, 0), ])

    def get_last_block(self):
        return self.chain[-1]

    def mine_pending_transaction(self, mining_reward_address):
        block = ABlock.ABlock(datetime.now(), self.pending_transactions)
        block.mine_block(self.difficulty)
        print('Block is mined --- ' + mining_reward_address + ' recieved ', self.mining_reward)
        self.chain.append(block)
        self.pending_transactions = [ATransaction.ATransaction(None, mining_reward_address, self.mining_reward)]

    def create_transaction(self, T):
        self.pending_transactions.append(T)

    def get_balance(self, address):
        balance = 0
        for b in self.chain:
            for t in b.transaction_list:
                if t.to_address == address:
                    balance += t.amount
                if t.from_address == address:
                    balance -= t.amount
        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            prevb = self.chain[i - 1]
            currb = self.chain[i]
            if currb.hash != currb.calc_hash():
                print('Invalid block')
                return False
            if currb.prev_hash != prevb.hash:
                print('Invalid chain')
                return False
        return True
