class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        curr_node = self.head
        while (curr_node):
            print(curr_node.data,end=" ")
            curr_node = curr_node.next

    def insert(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node


    def reverse_iterarive(self):
        prev=None
        curr=self.head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

    def reverse_recursive(self):
        def reverse_recursive(cur,prev):
            if not cur:
                return prev
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
            return reverse_recursive(cur,prev)
        self.head=reverse_recursive(cur=self.head,prev=None)
    def errorhandler(self):
        return "Invalid chioce"

if __name__ == '__main__':


    llist=linkedlist()
    llist.insert("A")
    llist.insert("B")
    llist.insert("C")
    llist.insert("D")
    llist.insert("E")
    print("linked list:")
    llist.printlist()
    # print("reverse recursive: ")
    # llist.reverse_recursive()
    # llist.printlist()
    print()
    print("Reverse iterative:")
    llist.reverse_iterarive()
    llist.printlist()

