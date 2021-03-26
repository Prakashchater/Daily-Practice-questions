class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cirlinkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        if self.head==None:
            print("The list is empty")
            return
        temp=self.head.next
        while(temp):
            print(temp.data)
            temp=temp.next
            if temp==self.head.next:
                break

    def addtoempty(self,data):
        if self.head!=None:
            return self.head
        newNode=node(data)
        self.head=newNode
        self.head.next=self.head
        return newNode

    def addtobegin(self,data):
        if self.head==None:
            return self.addtoempty(data)

        newNode=node(data)
        newNode.next=self.head.next
        self.head.next=newNode
        return self.head

    def addtoend(self,data):
        if self.head==None:
            return self.addtoempty(data)
        newNode=node(data)
        newNode.next=self.head.next
        self.head.next=newNode
        self.head=newNode
        return self.head

    def deletenode(self,key):
        if self.head.data==key:
            curr=self.head
            while(curr.next!=self.head):
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
        else:
            curr=self.head
            prev=None
            while(curr.next!=self.head):
                prev=curr
                curr=curr.next
                if curr.data==key:
                    prev.next=curr.next
                    curr=curr.next


if __name__ == '__main__':
    cllist=cirlinkedlist()
    # cllist.addtoempty("E")
    cllist.addtobegin("B")
    cllist.addtobegin("A")
    cllist.addtoend("C")
    cllist.addtoend("D")
    # cllist.deletenode("B")
    cllist.deletenode("D")
    cllist.printlist()


