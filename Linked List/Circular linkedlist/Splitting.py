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
    def printlist(self):
        curr=self.head
        while(curr):
            print(curr.data)
            curr=curr.next
            if curr==self.head:
                break
    def __len__(self):
        curr=self.head
        count=0
        while curr is not None:
            count+=1
            curr=curr.next
            if curr ==self.head:
                break
        return count

    def splitingnode(self):
        size=len(self)
        if size==0:
            return None
        if size == 1:
            return self.head
        mid=size//2
        count=0
        curr=self.head
        prev=None
        while (curr and count< mid):
            count+=1
            prev=curr
            curr=curr.next
        prev.next=self.head

        splitclist=cirlinkedlist()
        while curr.next!=self.head:
            splitclist.append(curr.data)
            curr=curr.next
        splitclist.append(curr.data)
        print("\nFirst Circular Linked List")
        self.printlist()
        print("\nSecond Circular Linked list")
        splitclist.printlist()

#A -> B -> C -> D -> E ->....
#A -> B -> and C -> D -> E ->....
if __name__ == '__main__':
    cllist=cirlinkedlist()
    cllist.append("A")
    cllist.append("B")
    cllist.append("C")
    cllist.append("D")
    cllist.append("E")
    cllist.append("F")
    # cllist.append("F")
    # cllist.printlist()
    cllist.splitingnode()
    # print(len(cllist))
    # cllist.printlist()
