"""
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
"""

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


if __name__ == '__main__':
    llist=linkedlist()
    llist.head=node(1)
    sec=node(2)
    third=node(3)
    ''' 
       Three nodes have been created. 
       We have references to these three blocks as head, 
       second and third 

       llist.head        second              third 
            |                |                  | 
            |                |                  | 
       +----+------+     +----+------+     +----+------+ 
       | 1  | None |     | 2  | None |     |  3 | None | 
       +----+------+     +----+------+     +----+------+ 
       '''

    llist.head.next=sec
    ''' 
    Now next of first Node refers to second.  So they 
    both are linked. 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
    sec.next=third
    ''' 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
    llist.printlist()

