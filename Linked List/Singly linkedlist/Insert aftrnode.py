class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head ==None

    def add(self,newdata):
        Temp = Node(newdata)
        #         What happens here: the Temp.Next is going to connect to the place that head is connected to
        Temp.setNext(self.head)
        self.head = Temp


    def printl(self):
        current = self.head
        i=""
        while current.getNext() != None:
            i =i+ "-"+str(current.getData())
            current= current.getNext()
        i =i+ "-"+str(current.getData())
        return i

    def insert(self, item, index):
        current = self.head
        counter = 0
        Temp = Node(item)

        Prev = None

        if index == 0:
            Temp.setNext(self.head)
            self.head = Temp
        else:
            while counter < index:
                Prev = current
                current = current.getNext()
                counter = counter+1

            Temp.setNext(Prev.getNext())
            Prev.setNext(Temp)
            current.setData = Temp

mylist = UnorderedList()
mylist.insert(54,0)
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
print(mylist.printl())
mylist.insert(12,0)
print(mylist.printl())