import random

data_keys = []

nodes = []

all_data =[]
class Data:
    def __init__(self,v,data_id):
        self.val = v
        self.key = data_id
        
    def addKey(self):
        val_key = random.randint(1,32)
        while(val_key in data_keys):
            val_key = random.randint(1,32)
        data_keys.append(val_key)
        return val_key
    

class Node:
    def __init__(self,id_test):
        # self.id = self.addId()
        self.id = id_test #this is for test , mesale Ostad
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
            temp = (self.id + 2**(i)) % nodes[len(nodes)-1].id 
            if (temp ==0):
                temp = nodes[len(nodes)-1].id
            # print("ID: "+str(self.id)+ ", row: "+ str(i)+", temp: " + str(temp) + ", Chape %:" + str(self.id + 2**(i)) +", raste %:"+ str(nodes[len(nodes)-1].id ))
            counter = 0
            while (counter < len(nodes)):
                if(nodes[counter].id >= temp):
                    
                    self.ft.append(nodes[counter].id)
                    break
                counter += 1
            i += 1
        
    def __str__(self):
        # s = [self.id,self.pred,self.succ,self.datas,self.ft]
        s = [self.id,self.ft]
        listToStr = ' ,'.join([str(elem) for elem in s]) 
        return listToStr

class Chord():
    def __init__(self):
        nodes_num = 32

    def addNode(self,id_test):
        peer = Node(id_test)
        nodes.append(peer)
        nodes.sort(key=lambda x: x.id)   
        peer.pred_cal(nodes.index(peer)) 
        peer.succ_cal(nodes.index(peer))

        
        

       
        if(len(nodes) > 1):
            peer.succ.pred = peer
            peer.pred.succ = peer
            self.updateDataOnAdd(peer) #data az node badi miad to node jadid
        
        # peer.FingerTable()
        # print("\n NEW ROUND new peer: " +str(id_test) +"\n") #Debugger

        # baraye update kardan finger table
        counter = 0
        i = nodes.index(peer)
        while(counter < 6 and i >= 0):
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

    def dataAdder(self,value,data_id):
        new_data = Data(value,data_id)
        
            
        #where data should go
        for i in range(len(nodes)):
            if(new_data.key <= nodes[i].id):
                nodes[i].datas.append(new_data)
                break
        all_data.append(new_data)
    def lookup(self,node_id,data_key):
        #test : node_id == 1 , data_key == 26
        for i in range(len(nodes)):
            if(nodes[i].id == node_id):
                peer = nodes[i]
        i =0  
        while( i < len(peer.ft)):
            print("peer.id: "+ str(peer.id) +", i: " + str(i))
            if(peer.ft[i] == data_key ):
                result_peer_id = peer.ft[i]
                
                for k in range(len(nodes)):
                    if( nodes[k].id == result_peer_id):
                        return nodes[k]

            elif(i == len(peer.ft)-1  and peer.ft[i] < data_key): # vaghty khune akhar FT mishe 18 va data_key == 26 va bayad berim peer jadid
                for j in range(len(nodes)): # searching for new peer
                    if(nodes[j].id == peer.ft[i]):
                        peer = nodes[j] #peer = 18
                        # print("HELLLLLLLLLLLLL "+ str(peer.id))
                        i = 0
            # elif(i != len(peer.ft)-1 and peer.ft[i] < data_key):
            #     i += 1 
            elif( i != 0 and peer.ft[i] > data_key):
                #vasate ft table idi bozorgtar az key mibinim pas ghablish ro bayad begirim
                for j in range(len(nodes)):
                    if(nodes[j].id == peer.ft[i-1]):
                        peer = nodes[j]
                        i = 0
            elif(i == 0 and peer.ft[i] > data_key):
                result_peer_id = peer.ft[i]
                
                for k in range(len(nodes)):

                    if( nodes[k].id == result_peer_id):
                        return nodes[k]
            
            else:
                i += 1
if __name__ == '__main__':
    
    net = Chord()
    net.addNode(1) # 1 is id of Node
    net.addNode(4) # 4 is id of Node
    net.addNode(9)
    net.addNode(11)
    net.addNode(14)
    net.addNode(18)
    net.addNode(20)
    net.addNode(21)
    net.addNode(28)

    net.dataAdder(2,3) # 2 value , 3 key
    net.dataAdder(6,4)
    net.dataAdder(1,26)
    net.dataAdder(12,20)
    net.dataAdder(26,12)
    net.dataAdder(20,21)

    temp = net.lookup(11,3)
    
    for i in range(len(nodes)):
        print(nodes[i])
        for x in nodes[i].datas:
            
            print(" key: " + str(x.key) )
    
    print("result : " + str(temp))
    # for i in range(len(all_data)): #Debugger DataAdder
    #     print("key: "+ str(all_data[i].key)+ ", value: "+ str(all_data[i].val))


    # for i in range(len(nodes)): #DEBUGGER succ and pred
        # print("Node.id: "+str(nodes[i].id)+", pred.id: "+ str(nodes[i].pred)+", succ.id: "+ str(nodes[i].succ))


        

