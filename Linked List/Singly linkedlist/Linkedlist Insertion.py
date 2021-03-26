"""
class node:
    def __init__(self,data):
        self. dat=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

#Add a node at the beginning        Time complexity: O(1)

    def push(self,new_data):
        new_node=node(new_data)             # 1 & 2: Allocate the Node & Put in the data
        new_node.next=self.head             # 3. Make next of new Node as head
        self.head=new_node                  # 4. Move the head to point to new Node


# Add a node after a given node       Time complexity: O(1)

    def insertafter(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node=node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

#Add a node at the end          Time complexity is O(N)

    def insertend(self,new_data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node=node(new_data)
        # 4. If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head=new_node
            return
        last=self.head      # 5. Else traverse till the last node
        while(last.next):
            last=last.next
        last.next=new_node      # 6. Change the next of last node

"""
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next

    def insertbegin(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node is nor there")
            return
        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertend(self, new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node


if __name__ == '__main__':
    llist=linkedlist()
    llist.insertend("A")
    llist.insertend("B")
    llist.insertend("D")
    llist.insertend("E")
    llist.append(llist.head.next,"C")
    print("Created list:")
    llist.printlist()













