class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        if self.head is None:
            return None
        else:
            temp=self.head
            while(temp):
                print(temp.data, end=" ")
                temp=temp.next

    def front(self,data):
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode

    def inBetween(self,prev,data):
        if prev is None:
            print("List is empty")
            return
        newNode=node(data)
        newNode.next=prev.next
        prev.next=newNode

    def end(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newNode

    def mergetwosorted(self,llist):
        p=self.head
        q=llist.head
        s=None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next

            else:
                s=q
                q=s.next
        new_head=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next

        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head

if __name__ == '__main__':
    llist_1=linkedlist()
    llist_2=linkedlist()

    llist_1.end(1)
    llist_1.end(3)
    llist_1.end(5)
    llist_1.end(7)
    llist_1.end(9)

    llist_2.end(2)
    llist_2.end(4)
    llist_2.end(6)
    llist_2.end(8)
    llist_2.end(10)

    # llist_1.printlist()
    # print()
    # llist_2.printlist()
    llist_1.mergetwosorted(llist_2)
    llist_1.printlist()