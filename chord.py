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
            node_counter += 1
        
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

    def FingerTable(self):
        row = 5
        i = 0
        self.ft =[]
        while( i < row ):
            temp = self.id + 2**(i-1) % nodes[len(nodes)-1].id 
            counter = 0
            while (counter < len(nodes)):
                if(nodes[counter].key >= temp):
                    self.ft.append(temp)
                    break
                counter += 1
            i += 1


class Chord():
    def __init__(self):
        nodes_num = 32

    def addNode(self):
        peer = Node()
        nodes.append(peer)
        nodes.sort(key=lambda x: peer.id)
        peer.pred_cal(nodes.index(peer)) 
        peer.succ_cal(nodes.index(peer))
        self.updateDataOnAdd(peer) #data az node badi miad to node jadid
        peer.FingerTable()

        # baraye update kardan finger table
        counter = 0
        i = nodes.index(peer)-1
        while(counter < 5 ):
            nodes[i].FingerTable()
            counter += 1 
            i -= 1

        

    def updateDataOnAdd(self,peer):
        next_node = peer.succ
        for i in range(len(next_node.datas)) :
            if(next_node.datas[i].key <= peer.id):
                peer.datas.append(next_node.datas[i])

    def deleteNode(self,id):
        del_peer = Node()
        peer_after = Node()
        peer_before = Node()
        for i in range(len(nodes)):
            if(nodes[i].id == id):
                del_peer = nodes[i]
                break
            else:
                return 

        #fixing Pred and succ
        peer_after = nodes[i+1]
        peer_before = nodes[i-1]
        peer_after.pred_cal(i-1)
        peer_before.succ_cal(i+1)
        #update data On delete
        peer_after.datas = peer_after.datas+del_peer.datas

        nodes.remove(del_peer)
        counter = 0
        i = nodes.index(del_peer)-1
        while(counter < 5 ): #update fingerTables of Previous Nodes
            nodes[i].FingerTable()
            counter += 1 
            i -= 1

    def dataAdder(self):
        new_data = Data()
        


        

