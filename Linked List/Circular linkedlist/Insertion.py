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

if __name__ == '__main__':
    cllist=cirlinkedlist()
    cllist.append(8)
    cllist.append(10)
    cllist.prepend(6)
    cllist.prepend(4)
    cllist.prepend(2)
    cllist.printlist()



#
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class cirlinkedlist:
#     def __init__(self):
#         self.head=None
#
#     def addatEmpty(self,data):
#         if (self.head!=None):
#             return self.head
#         newNode=node(data)
#         self.head=newNode
#         self.head.next=self.head
#         return self.head
#
#
#     def addBegin(self,data):
#         if (self.head==None):
#             return self.addatEmpty(data)
#         newNode=node(data)
#         newNode.next=self.head.next
#         self.head.next=newNode
#         return self.head
#
#     def addEnd(self,data):
#         if (self.head==None):
#             return self.addatEmpty(data)
#
#         newNode=node(data)
#         newNode.next=self.head.next
#         self.head.next=newNode
#         self.head=newNode
#         return self.head
#
#     def addinBetween(self,data,item):
#         if self.head==None:
#             return None
#         newNode=node(data)
#         p=self.head.next
#         while p:
#             if (p.data==item):
#                 newNode.next=p.next
#                 p.next=newNode
#
#                 if (p==self.head):
#                     self.head=newNode
#                     return self.head
#                 else:
#                     return self.head
#             p=p.next
#             if(p==self.head.next):
#                 print(item,"not present in the list")
#                 break
#
#     def printlist(self):
#         if self.head==None:
#             print("List is Empty")
#             return
#         curr=self.head.next
#         while(curr):
#             print(curr.data,end=" ")
#             curr=curr.next
#             if curr == self.head.next:
#                 break
#
#
# if __name__ == '__main__':
#     cllist=cirlinkedlist()
#
#     cllist.addatEmpty(6)
#     cllist.addBegin(4)
#     cllist.addBegin(2)
#     cllist.addEnd(8)
#     cllist.addEnd(12)
#     cllist.addinBetween(10,8)
#     cllist.printlist()














