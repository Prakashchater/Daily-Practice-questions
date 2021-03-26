class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Linked list is Empty.!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.next

    def add_begin(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_afterNode(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not present in LL.")
        else:
            new_node = node(data)
            new_node.next = n.next
            n.next = new_node

    def add_beforeNode(self,data,x):
        if self.head is None:
            print("Linked List is Empty!")
            return
        # If we want to add before the head..
        if self.head.data == x:
            new_node = node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        # If we want to add before any other nodes...
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node not Found!")
        else:
            new_node = node(data)
            new_node.next = n.next
            n.next = new_node


    def deletion_begin(self):
        if self.head is None:
            print("Linked list is Empty!")
        else:
            self.head = self.head.next

    def deletion_end(self):
        if self.head is None:
            print("Linked list is empty!")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_atValue(self,x):
        if self.head is None:
            print("LL is Empty!")
            return
        if x == self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.next.data:
                break
            n = n.next
        if n.next is None:
            print("LL is not Present.")
        else:
            n.next = n.next.next

#Calculating the length of the linked list
    def len_iterative(self):
        count=0
        curr_node = self.head
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        return count

#Searching an element in the Linked list
    def search(self, x):
        n = self.head
        while n is not None:
            if n.data == x:
                return True
            n = n.next
        return False



if __name__ == '__main__':
    LL = singlyLinkedList()
    LL.add_begin(20)
    LL.add_begin(30)
    LL.add_begin(10)
    LL.add_end(60)
    LL.add_beforeNode(40,10)
    LL.add_beforeNode(50,30)
    LL.deletion_end()
    # LL.delete_atValue(50)
    print(LL.search(60))
    print(LL.len_iterative())
    LL.traversal()



