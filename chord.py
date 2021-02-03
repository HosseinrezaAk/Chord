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

    def pred_cal(self,peer_index):
        pred_index = None
        if(peer_index == 0 ):
            if(len(nodes) == 1):
                return 
            else:
                pred_index = len(nodes) - 1
                self.pred = nodes[peer_index]

        else:
            pred_index = peer_index - 1 
            self.pred = nodes[pred_index]
    
    def succ_cal(self, peer_index):
        succ_index =None
        if(peer_index == len(nodes)-1):
            if(len(nodes) == 1 ):
                return
            else:
                succ_index = 0
                self.succ = nodes[succ_index]
        else:
            succ_index = peer_index + 1
            self.succ = nodes[succ_index]


class Chord():
    def __init__(self):
        nodes_num = 32

    def addNode(self):
        peer = Node()
        nodes.append(peer)
        nodes.sort(key=lambda x: peer.id)
        peer.pred_cal(nodes.index(peer)) 
        peer.succ_cal(nodes.index(peer))
        
    def updateDataOnAdd(self,peer):
        next_node = peer.succ
        for i in range(len(next_node.datas)) :
            if(next_node.datas[i].key <= peer.id):
                peer.datas.append(next_node.datas[i])

    def deleteNode():
        pass

    def
