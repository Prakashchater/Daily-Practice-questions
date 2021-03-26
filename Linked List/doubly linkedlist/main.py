class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def forwardTraversal(self):
        if self.head is None:
            print("Linked list is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.next

    def backwardTraversal(self):
        if self.head is None:
            print("Linked list is Empty!")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.prev

    def add_empty(self,data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
        else:
            print("Linked list is empty!")

    def add_begin(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            new_node.prev = n

    def add_after(self,data,x):
        if self.head is None:
            print("DLl is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Given node is not present in DLL.")
            else:
                new_node = node(data)
                new_node.next = n.next
                new_node.prev = n
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("DLl is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Given node is not present in DLL.")
            else:
                new_node = node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                else:
                    self.head = new_node
                n.prev = new_node

    def delete_begin(self):
        if self.head is None:
            print("DLL is empty, can't Delete !")
            return
        # when DLL have only one node
        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting the node!")
        # When DLL have more than one node
        else:
            self.head = self.head.next
            self.head.prev = None


    def delete_end(self):
        if self.head is None:
            print("DLL is empty, can't Delete !")
            return
        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting the node!")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prev.next = None


    def delete_byValue(self,x):
        if self.head is None:
            print("DLL is empty, can't delete!")
            return
        # When we delete only one node.
        if self.head.next is None:
            if self.head.data == x:
                self.head = None
            else:
                print("data is not present in the node.")
            return
        # deleting the first node in more than one node
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return
        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
        # deleting the middle node
        if n.next is not None:
            n.next.prev = n.prev
            n.prev.next = n.next
        else:
            if n.data == x:
                n.prev.next = None
            else:
                print("x is not present in the node.")


DLL = doublyLinkedList()
# DLL.add_empty(10)
DLL.add_begin(20)
DLL.add_end(30)
DLL.add_end(100)
# DLL.add_after(20,20)
# DLL.add_before(200,20)
# DLL.delete_begin()
# DLL.delete_end()
DLL.delete_byValue(1100)
# print("Forward Traversal:")
DLL.forwardTraversal()
# print("\nReverse Traversal:")
print()
DLL.backwardTraversal()



