# O(v+e) time | O(v) space
class node:
    def __init__(self,name):
        self.children=[]
        self.name= name

    def ischild(self,name):
        self.children.append(node(name))

    def breadthfirstsearch(self,array):
        queue=[self]
        while len(queue) > 0:
            current= queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


