class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublinkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next


    def prepend(self,data):
        if self.head is None:
            newNode=node(data)
            newNode.prev=None
            self.head=newNode
        else:
            newNode=node(data)
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
            newNode.prev=None

    def append(self,data):
        if self.head is None:
            newNode=node(data)
            newNode.prev=None
            self.head=newNode
        else:
            newNode=node(data)
            curr=self.head
            while curr.next :
                curr=curr.next
            curr.next=newNode
            newNode.next=None
            newNode.prev=curr

    def removal(self,key):
        curr=self.head
        while curr is not None:
            if curr.data== key and curr == self.head:
                if not curr.next:
                    curr=None
                    self.head=None
                    return

                #Case 2
                else:
                    nxt=curr.next
                    curr.next=None
                    nxt.prev=None
                    curr=None
                    self.head=nxt
                    return

            elif curr.data==key:
                #Case 3
                if curr.next:
                    nxt=curr.next
                    prev=curr.prev
                    prev.next=nxt
                    nxt.prev=prev
                    curr.next=None
                    curr.prev=None
                    curr=None
                    return

                # Case 4
                else:
                    prev=curr.prev
                    prev.next=None
                    curr.prev=None
                    curr=None
                    return
        curr=curr.next





    # def transverse(self,Node):
    #     print("\nTraverse in forward direction")
    #     while (Node is not None):
    #         print(Node.data,end=" ")
    #         last = Node
    #         Node = Node.next
    #     print("\nTraverse in reverse direction")
    #     while (last is not None):
    #         print(last.data,end=" ")
    #         last = last.prev


if __name__ == '__main__':
    dllist=doublinkedlist()
    # 1 -> 2 -> 3 -> 4 -> 5 ->....
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.append(5)
    dllist.removal(1)
    # dllist.removal(4)
    # dllist.transverse(dllist.head)
    # print()
    dllist.printlist()


