class node:

    def __init__(self,name):
        self.children=[]
        self.name= name
    def addchild(self,name):
        self.children.append(node(name))

    def depthfirstsearch(self,array):
        array.append(self.children)
        for child in self.children:
            self.depthfirstsearch(array)
        return array

