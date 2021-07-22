class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class LinkedListInsertion:
    # create of object  head at  pointer is null
    def __init__(self):
        self.head=None

    def insert_at_begining(self,key):
        new_node=Node(key)
        new_node.next=self.head
        self.head=new_node

    def insert_at_specific_postion(self,node_after,key):
        
