class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def printlist(self):
        curr_node=self.head
        while(curr_node):
            print(curr_node.data)
            curr_node=curr_node.next
    def push(self,data):
        curr_node=node(data)
        curr_node.next=self.head
        self.head=curr_node
    def append(self,prev_node,data):
        if prev_node is None:
            print("Previous node is not present")
            return
        curr_node=node(data)
        curr_node.next=prev_node.next
        prev_node.next=curr_node
    def end(self,data):
        curr_node=node(data)
        if self.head is None:
            self.head=curr_node
            return
        last_node=self.head
        while(last_node.next):
            last_node=last_node.next
        last_node.next=curr_node
    # def deletenode(self,key):
    #     curr_node=self.head
    #     if (curr_node and curr_node.data==key):
    #         self.head=curr_node.next
    #         curr_node=None
    #         return
    #     prev=None
    #     while(curr_node and curr_node.data!=key):
    #         prev=curr_node
    #         curr_node=curr_node.next
    #     if curr_node is None:
    #         return
    #     prev.next=curr_node.next
    #     curr_node=None

    def delete_at_pos(self,position):
        if self.head == None:
            return
        curr_node=self.head
        if position==0:
            self.head=curr_node.next
            curr_node=None
            return
        for i in range(position-1):
            curr_node=curr_node.next
            if curr_node is None:
                break
        if (curr_node and curr_node.next== None):
            return
        next=curr_node.next.next
        curr_node.next=None
        curr_node.next=next


if __name__ == '__main__':
    llist=ll()
    llist.push(7)
    llist.push(6)
    llist.end(9)
    llist.end(10)
    llist.append(llist.head.next,8)
    llist.printlist()
    # llist.deletenode(10)
    # print("deleted element:")
    # llist.printlist()
    llist.delete_at_pos(2)
    print("linked list deleting at the pos 2:")
    llist.printlist()

