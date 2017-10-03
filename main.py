#!/usr/bin/env python3
from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = sha256()
        data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash)
        sha.update(data.encode())
        return sha.hexdigest()


class Blockchain:
    def __init__(self, init_hash='0'):
        self.chain = [self._create_genesis_block(init_hash)]

    def __str__(self):
        res = []
        for block in self.chain:
            res.append('Block #{}:'.format(block.index))
            res.append('    Data:      {}'.format(block.data))
            res.append('    Timestamp: {}'.format(block.timestamp))
            res.append('    Hash:      {}'.format(block.hash))
            res.append('')
        return '\n'.join(res)

    @staticmethod
    def _create_genesis_block(init_hash):
        return Block(0, datetime.now(), 'Genesis block', init_hash)

    def _next_block(self, data):
        prev_block = self.chain[-1]
        return Block(
            index=prev_block.index + 1,
            timestamp=datetime.now(),
            data=data,
            prev_hash=prev_block.hash
        )

    def add_block(self, data=''):
        self.chain.append(self._next_block(data))


if __name__ == '__main__':
    print('Creating test blockchain...')
    bc = Blockchain()
    for i in range(20):
        bc.add_block('Hello, I am block :)')
    print(bc)
