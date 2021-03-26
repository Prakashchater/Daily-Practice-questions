class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cirlinkedlist:
    def __init__(self):
        self.head=None
    def prepend(self,data):
        newNode=node(data)
        curr=self.head
        newNode.next=self.head
        if not self.head:
            newNode.next=newNode
        else:
            while(curr.next!=self.head):
                curr=curr.next
            curr.next=newNode
        self.head=newNode

    def append(self,data):
        if not self.head:
            self.head=node(data)
            self.head.next=self.head
        else:
            newNode=node(data)
            curr=self.head
            while(curr.next!=self.head):
                curr=curr.next
            curr.next=newNode
            newNode.next=self.head
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode

    def printlist(self):
        if self.head==None:
            print("List is empty")
            return
        curr=self.head.next
        while curr is not None:
            print(curr.data)
            curr=curr.next
            if curr.next==self.head:
                break


    def isCircularLinkedlist(self,inputdata):
        curr=inputdata.head
        while curr.next is not None:
            curr=curr.next
            if curr.next == inputdata.head:
                return True
        return False


if __name__ == '__main__':

    llist=linkedlist()
    llist.insert(4)
    llist.insert(3)
    llist.insert(2)
    llist.insert(1)

    cllist=cirlinkedlist()
    cllist.append(1)
    cllist.append(2)
    cllist.append(3)
    cllist.append(4)
    print(llist.isCircularLinkedlist(llist))
    print(llist.isCircularLinkedlist(cllist))






