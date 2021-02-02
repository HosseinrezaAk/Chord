import random

data_keys = []
node_ids = []
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
        self.id = self.addId()
        self.pred = None
        self.succ = None
        self.datas = []
        self.ft = []

    def addId(self):
        val_id = random.randint(1,32)
        while(val_id in node_ids):
            val_id = random.randint(1,32)
        node_ids.append(val_id)
        return val_id