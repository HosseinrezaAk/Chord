import random

class Data:
    def __init__(self,v):
        self.val = v
        self.key = random.randrange(1, 32)
    
    

class Node:
    def __init__(self):
        