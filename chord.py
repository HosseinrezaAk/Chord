import random

data_keys = []

nodes = []
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
        node_counter =0

        while( node_counter > len(nodes) ):
            if(nodes[node_counter].id == val_id):
                    val_id = random.randint(1,32)
        
        return val_id

    def pred_cal(self):
        
        if (len(node_ids) == 1):
            return 
        else:
class Chord():
    def __init__(self):
        nodes_num = 32

    def addNode(self):
        peer = Node()
        nodes.append(peer)
        nodes.sort(key=lambda x: peer.id)
        peer.pred_cal() #To do
        

    def deleteNode():
        pass

    def
