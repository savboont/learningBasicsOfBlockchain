from time import time
from hashlib import sha256
import json


class Block:

	def __init__(self, timestamp=None, data=None):
		self.timestamp = timestamp or time()
		self.data = [] if data is None else data
		self.prevHash = None
		self.nonce = 0
		self.hash = self.getHash()

	def getHash(self):
		hash = sha256()
		hash.update(str(self.prevHash).encode('utf-8'))
		hash.update(str(self.timestamp).encode('utf-8'))
		hash.update(str(self.data).encode('utf-8'))
		hash.update(str(self.nonce).encode('utf-8'))
		return hash.hexdigest()

	def mine(self, difficulty):
		while self.hash[:difficulty] != '0' * difficulty:
			self.nonce += 1
			self.hash = self.getHash()


class Blockchain:

	def __init__(self):
		self.chain = [Block(str(int(time())))]
		self.difficulty = 1
		self.blockTime = 30000

	def get_last_block(self):
		return self.chain[len(self.chain) - 1]

	def add_block(self, block):
		block.prevHash = self.get_last_block().hash
		block.hash = block.getHash()
		block.mine(self.difficulty)
		self.chain.append(block)

		self.difficulty += (-1, 1)[int(time()) - int(self.get_last_block().timestamp) < self.blockTime]

	def is_valid(self):
		for i in range(1, len(self.chain)):
			current_block = self.chain[i]
			prev_block = self.chain[i - 1]

			if current_block.hash != current_block.getHash() or prev_block.hash != current_block.prevHash:
				return False

		return True

	def __repr__(self):
		return json.dumps([{'data': item.data, 'timestamp': item.timestamp, 'nonce': item.nonce, 'hash': item.hash, 'prevHash': item.prevHash} for item in self.chain], indent=4)