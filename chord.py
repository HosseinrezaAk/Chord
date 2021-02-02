import random


data_keys = []
class Data:
    def __init__(self,v):
        self.val = v
        self.key = self.addKey()
    
    def addKey(self):
        val_key = random.randint(1,32)
        while(val_key in data_keys):
            val_key = random.randint(1,32)
        
        data_keys.append(val_key)
        return val_key


class Node:
    def __init__(self):
        