import random


data_keys = []
class Data:
    def __init__(self,v):
        self.val = v
        self.key = self.addKey()
    
    def addKey(self):

        self.key = random.randint(1,32)
        while(self.key in data_keys):
            self.key = random.randint(1,32)
    
        data_keys.append(self.key)


class Node:
    def __init__(self):
        