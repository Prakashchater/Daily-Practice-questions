class node:
    def __init__(self,value):
        self.value=value
        self.left= None
        self.right= None
class binarytree:
    def __init__(self,root):
        self.root=node(root)

    def printtree(self,traversal_type):
        if traversal_type== "inorder":
            return self.inorder(tree.root, " ")
        elif traversal_type=="preorder":
            return self.preorder(tree.root," ")
        elif traversal_type=="postorder":
            return self.postorder(tree.root," ")

        else:
            print("traversal_type"+ str(traversal_type)+ "not supported. ")

    def inorder(self,start,traversal):
        """Left-Root-Right"""
        if start:
            traversal= self.inorder(start.left, traversal)
            traversal+=(str(start.value)+ "-")
            traversal=self.inorder(start.right, traversal)
        return traversal

    def preorder(self,start,traversal):
        """Root-left-Right"""
        if start:
            traversal+=(str(start.value)+ "-")
            traversal=self.preorder(start.left, traversal)
            traversal=self.preorder(start.right, traversal)
        return traversal

    def postorder(self,start,traversal):
        """left-Right-Root"""
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal = self.inorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

if __name__ == '__main__':
    tree=binarytree(1)
    tree.root.left=node(2)
    tree.root.right=node(3)
    tree.root.left.left=node(4)
    tree.root.left.right=node(5)
    tree.root.right.left=node(6)
    tree.root.right.right=node(7)

    print(tree.printtree("inorder"))
    print(tree.printtree("preorder"))
    print(tree.printtree("postorder"))