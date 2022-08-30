from blockchain import Blockchain, Block
from time import time


JeChain = Blockchain()

JeChain.add_block(Block(str(int(time())), ({"from": "John", "to": "Bob", "amount": 100})))

print(JeChain)