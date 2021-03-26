class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data)
                temp=temp.next
    def insertbegin(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node


    def append(self,prev_node,new_data):
        if prev_node is None:
            print("Previous node is nor there")
            return
        new_node=node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node


    def insertend(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node

    def deletenode(self,key):
        curr_node=self.head
        if (curr_node and curr_node.data==key):
            self.head= curr_node.next
            curr_node=None
            return
        prev=None
        while(curr_node and curr_node.data!=key):
            prev=curr_node
            curr_node=curr_node.next
        if curr_node is None:
            return
        prev.next=curr_node.next
        curr_node=None

if __name__ == '__main__':
    llist=linkedlist()
    llist.insertend("A")
    llist.insertend("B")
    llist.insertend("C")
    llist.insertend("D")
    print("Created list:")
    llist.printlist()
    llist.deletenode("B")
    print("Deleted node in a list is:")
    llist.printlist()


