class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        curr_node=self.head
        while(curr_node):
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
    def insert(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def swapping_nodes(self,key1,key2):
        if key1==key2:
            return
        prev1=None
        curr1=self.head
        while curr1 and curr1.data!= key1:
            prev1=curr1
            curr1=curr1.next
        prev2=None
        curr2=self.head
        while(curr2 and curr2.data!=key2):
            prev2=curr2
            curr2=curr2.next
        if curr1 and curr2 == None:
            return
        if prev1!=None:
            prev1.next=curr2
        else:
            self.head=curr2
        if prev2!=None:
            prev2.next=curr1
        else:
            self.head=curr1
        curr1.next,curr2.next=curr2.next,curr1.next


llist=linkedlist()
llist.insert("A")
llist.insert("B")
llist.insert("C")
llist.insert("D")
print("linked list:")
llist.printlist()
print()
print("swap nodes: ")
llist.swapping_nodes("B","A")
llist.printlist()

