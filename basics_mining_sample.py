# ##############################
# Basics of BlockChain
# with a purpose of using blockchain technique in deep learing methods
# By Ahmad Karambakhsh
# ##############################

from ABlockChain_basics import ABlockChain,ATransaction


abc = ABlockChain.ABlockChain()
abc.create_transaction(ATransaction.ATransaction('user1', 'user2', 100))
abc.create_transaction(ATransaction.ATransaction('user2', 'user1', 50))
abc.mine_pending_transaction('miner')
abc.create_transaction(ATransaction.ATransaction('user1', 'user2', 100))
abc.create_transaction(ATransaction.ATransaction('user2', 'user1', 50))
abc.mine_pending_transaction('user2')
abc.mine_pending_transaction('miner')
abc.mine_pending_transaction('miner')
print('miner balance is ', abc.get_balance('miner'))
print('user2 balance is ', abc.get_balance('user2'))