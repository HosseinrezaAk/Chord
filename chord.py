
'''
Hosseinreza Akbari
9533840

I have both English and Persian comments ,
 in different situation I prefer type in persian like Long sentences.
'''



import random
from threading import Lock, Condition, Thread


data_keys = []
nodes = []
all_data =[] # this was for testing truthness of Data assigning 

class Data:
    ''' 
        Man baraye Test codam ro az halate dynamic dar ovordam ke betunam rahat testesh konam
        vali agar mikhahid be soorate dynamic kar konad kafist bejaye "data_id" dar khate 
        26 function "addkey()" ra ezaf konid va dar oon halat faghat bayad hengame seda zadan
        dataAdder() 1 variable be an pass dahid.

    '''
    def __init__(self,v):
        self.val = v
        # self.key = data_id
        self.key = self.addKey()
        
    def addKey(self):
        val_key = random.randint(1,32)
        while(val_key in data_keys):
            val_key = random.randint(1,32)
        data_keys.append(val_key)
        return val_key
    

class Node:
    '''
        inja ham b hamin shekl , Karkarde class kamelan vazehe va baraye test man
        karkard datagiri ro avaz kardm ke betunam be soorate dasti az daste Main betunam vared konam
        vali dar Funtionality code hich taghiri ijad nashode va doros kar miknad
    '''
    def __init__(self):
        self.id = self.addId()
        # self.id = id_test #this is for test , mesale Ostad
        self.pred = None
        self.succ = None
        self.datas = []
        self.ft = []

    def addId(self):

        val_id = random.randint(1,32)
        node_counter =0

        while( node_counter < len(nodes) ):
            if(nodes[node_counter].id == val_id):
                    val_id = random.randint(1,32)
                    node_counter = 0
            else:
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
        # listToStr = ' ,'.join([str(elem) for elem in s]) 
        listToStr = "\n### Node ID: "+ str(self.id)+ ", FingerTable: "+ str(self.ft)
        return listToStr

class Chord():
    def __init__(self):
        nodes_num = 32
        
    def addNode(self):
        monitor.Lock_Add_Delete()

        peer = Node()
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

        monitor.Release_Add_Delete()
    def updateDataOnAdd(self,peer):
        next_node = peer.succ
        for i in range(len(next_node.datas)) :
            if(next_node.datas[i].key <= peer.id):
                peer.datas.append(next_node.datas[i])

    def deleteNode(self,id):
        monitor.Lock_Add_Delete
        
        for i in range(len(nodes)):
            if(nodes[i].id == id):
               
                del_peer = nodes[i]
                break
            

        #fixing Pred and succ
        peer_after = nodes[i+1]
        peer_before = nodes[i-1]

        peer_after.pred = peer_before
        peer_before.succ = peer_after
        #update data On delete
        peer_after.datas = peer_after.datas+del_peer.datas
       
        i = nodes.index(del_peer)-1

        nodes.remove(del_peer)

        counter = 0
        
        while(counter < 5 ): #update fingerTables of Previous Nodes
            nodes[i].FingerTable()
            counter += 1 
            i -= 1
        monitor.Release_Add_Delete()
    def dataAdder(self,value):
        monitor.Lock_DataAdder()

        new_data = Data(value)
        #where data should go
        for i in range(len(nodes)):
            if(new_data.key <= nodes[i].id):
                nodes[i].datas.append(new_data)
                break
        all_data.append(new_data)

        monitor.Release_DataAdder()
    def lookup(self,node_id,data_key):
        #test : node_id == 1 , data_key == 26
        monitor.Lock_LookUp()

        for i in range(len(nodes)):
            if(nodes[i].id == node_id):
                peer = nodes[i]
        i =0  
        while( i < len(peer.ft)):
            # print("peer.id: "+ str(peer.id) +", i: " + str(i)) #DEBUGGER
            if(peer.ft[i] == data_key ):
                result_peer_id = peer.ft[i]
                
                for k in range(len(nodes)):
                    if( nodes[k].id == result_peer_id):
                        print("Data: "+str(data_key)+" is in: --> "+ "Node: "+str(nodes[k].id))
                        return nodes[k]

            elif(i == len(peer.ft)-1  and peer.ft[i] < data_key): # vaghty khune akhar FT mishe 18 va data_key == 26 va bayad berim peer jadid
                for j in range(len(nodes)): # searching for new peer
                    if(nodes[j].id == peer.ft[i]):
                        peer = nodes[j] #peer = 18 
                        i = 0
                        break
            elif( i != 0 and peer.ft[i] > data_key):
                #vasate ft table idi bozorgtar az key mibinim pas ghablish ro bayad begirim
                for j in range(len(nodes)):
                    if(nodes[j].id == peer.ft[i-1]):
                        peer = nodes[j]
                        i = 0
                        break
            elif(i == 0 and peer.ft[i] > data_key):
                result_peer_id = peer.ft[i]            
                for k in range(len(nodes)):
                    if( nodes[k].id == result_peer_id):
                        print("Data: "+str(data_key)+" is in: --> "+ "Node: "+str(nodes[k].id))
                        return nodes[k]
            else:
                i += 1

        monitor.Release_LookUp()


class Monitor:

    '''
        Class monitor karaiii in kelas baraye ghesmate Hamravandi hast va 
        az nazare implementation mesle code ke sare kelas tozih dadin mibashad
    '''
    def __init__(self):
        self.data_adder_counter = 0
        self.busy = False
        self.lookup_counter = 0
        self.lookup_queue = Condition() 
        self.dataAdder_queue = Condition()
        self.add_delete_queue = Condition() 
        self.mutex = Lock()

    def Lock_LookUp(self):

        self.lookup_queue.acquire()
        self.mutex.acquire()
        while self.busy:
            self.mutex.release()
            self.lookup_queue.wait()
            self.mutex.acquire()
        self.lookup_counter += 1
        self.mutex.release()
        self.lookup_queue.notifyAll()
        self.lookup_queue.release()
    def Release_LookUp(self):

        self.lookup_queue.acquire()
        self.mutex.acquire()
        self.lookup_counter -= self.lookup_counter
        if self.lookup_counter == 0:
            self.dataAdder_queue.acquire()
            self.dataAdder_queue.notify()
            self.dataAdder_queue.release()
            self.add_delete_queue.acquire()
            self.add_delete_queue.notify()
            self.add_delete_queue.release()
        self.mutex.release()
        self.lookup_queue.release()

    def Lock_DataAdder(self):
        self.dataAdder_queue.acquire()
        self.mutex.acquire()
        while self.busy:
            self.mutex.release()
            self.dataAdder_queue.wait()
            self.mutex.acquire()
        self.data_adder_counter += 1
        self.mutex.release()
        self.dataAdder_queue.notifyAll()
        self.dataAdder_queue.release()

    def Release_DataAdder(self):

        self.dataAdder_queue.acquire()
        self.mutex.acquire()
        self.data_adder_counter -= self.data_adder_counter
        if self.data_adder_counter == 0:
            self.lookup_queue.acquire()
            self.lookup_queue.notify()
            self.lookup_queue.release()

            self.add_delete_queue.acquire()
            self.add_delete_queue.notify()
            self.add_delete_queue.release()
        self.mutex.release()
        self.dataAdder_queue.release()

    def Lock_Add_Delete(self):
        self.add_delete_queue.acquire()
        self.mutex.acquire()
        while self.busy or self.data_adder_counter > 0 or self.lookup_counter > 0:
            self.mutex.release()
            self.add_delete_queue.wait()
            self.mutex.acquire()
        self.busy = True
        self.mutex.release()
        self.add_delete_queue.release()
        
    def Release_Add_Delete(self):
        self.add_delete_queue.acquire()
        self.dataAdder_queue.acquire()
        self.lookup_queue.acquire()
        self.mutex.acquire()
        self.busy = False
        self.mutex.release()
        self.add_delete_queue.notify()
        self.add_delete_queue.release()
        self.dataAdder_queue.notify()
        self.dataAdder_queue.release()
        self.lookup_queue.notify()
        self.lookup_queue.release()

monitor = Monitor()

if __name__ == '__main__':
    
    net = Chord()

    '''
    net.addNode(1) # 1 is id of Node
    net.addNode(4) # 4 is id of Node
    net.addNode(9)
    net.addNode(11)
    net.addNode(14)
    net.addNode(18)
    net.addNode(20)
    net.addNode(21)
    net.addNode(28)
    '''
    
    addList_nodes = []
    for i in range(9):
        addList_nodes.append(Thread(target=net.addNode))
    for i in range(9):
        addList_nodes[i].start()
    for i in range(9):
        addList_nodes[i].join()

    # for i in range(len(nodes)):
    #     print(nodes[i])
    
    addList_data =[]
    for i in range(15):
        addList_data.append(Thread(target=net.dataAdder, args = [random.randint(1,50)]))
    for i in range(15):
        addList_data[i].start()
    for i in range(15):
        addList_data[i].join()

    for i in range(len(nodes)):
        print(nodes[i])
        for x in nodes[i].datas:
            print("$ Data key: " + str(x.key) + ", Data value: "+ str(x.val) )

    lookup_list = []
    print("Search? (y/n)")
    #
    usr_in = input()
    while usr_in == "y":
        
        peer_id = int(input("Node ID: "))
        data_key = int(input("Data Key: "))
        lookup_list.append(Thread(target=net.lookup, args=[peer_id, data_key]))
        print("More searching? (y/n) ")
        usr_in = input()

    for i in range(len(lookup_list)):
        lookup_list[i].start()
    for i in range(len(lookup_list)):
        lookup_list[i].join()


    delete_list = []
    print("Wanna Delete Node?(y/n)")
    usr_in = input()
    while usr_in == "y":
        peer_id = int(input("Node ID: "))
        delete_list.append(Thread(target=net.deleteNode, args=[peer_id]))
        print("More Deleting? (y/n)")
        usr_in = input()

    for i in range(len(delete_list)):
        delete_list[i].start()
    for i in range(len(delete_list)):
        delete_list[i].join()

    for i in range(len(nodes)):
        print(nodes[i])
        for x in nodes[i].datas:
            print("$ Data key: " + str(x.key) + ", Data value: "+ str(x.val) )


    '''
    net.dataAdder(2,3) # 2 value , 3 key
    net.dataAdder(6,4)
    net.dataAdder(1,26)
    net.dataAdder(12,20)
    net.dataAdder(26,12)
    net.dataAdder(20,21)
    net.dataAdder(15,17) # this is for checking update the Dataset after Deleting Node 18

    # net.dataAdder(2)  # this is example of dynamic dataAdder as I explained in DataClass

    temp = net.lookup(1,26) # THis is lookUp example
    
    net.deleteNode(18) 

    for i in range(len(nodes)):
        print(nodes[i])
        for x in nodes[i].datas:
            
            print("Data key: " + str(x.key) + ", Data value: "+ str(x.val) )
    
    print("\nresult for Look Up : " + str(temp)) # this is the result of lookUp
    '''


'''
in some Lines of code i have # DEbugger 
 ,you can use them to see what is happening in details if u want
 ,otherwise ignore them.
'''


    # for i in range(len(all_data)): #Debugger DataAdder
    #     print("key: "+ str(all_data[i].key)+ ", value: "+ str(all_data[i].val))


    # for i in range(len(nodes)): #DEBUGGER succ and pred
        # print("Node.id: "+str(nodes[i].id)+", pred.id: "+ str(nodes[i].pred)+", succ.id: "+ str(nodes[i].succ))


        

