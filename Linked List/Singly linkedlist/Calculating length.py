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

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1+self.len_recursive(node.next)

    def len_iterative(self):
        count=0
        curr_node=self.head
        while(curr_node):
            count+=1
            curr_node=curr_node.next
        return count


if __name__ == '__main__':
    llist=linkedlist()
    llist.insertend("A")
    llist.insertend("B")
    llist.insertend("D")
    llist.insertend("E")
    llist.append(llist.head.next,"C")
    # print("Created list:")
    # llist.printlist()
    print(llist.len_recursive(llist.head))
    print(llist.len_iterative())