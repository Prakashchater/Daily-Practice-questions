class node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinaryTree(object):
    def __init__(self,root):
        self.root= node(root)

    def print_tree(self,traversal_type):
        if traversal_type== "preorder":
            return self.preorder(tree.root, "")
        elif traversal_type== "inorder":
            return self.inorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder(tree.root,"")
        else:
            print("traverasal_type "+ str(traversal_type)+ "is not supported")

    def preorder(self,start,traversal):
        """Root-left-right"""
        if start:
            traversal+=(str(start.value) + "-")
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal

    def inorder(self,start,traversal):
        """Left-Root-Right"""
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=(str(start.value)+ "-")
            traversal=self.inorder(start.right,traversal)
        return traversal

    def postorder(self,start,traversal):
        """Left-Right-Root"""
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal=self.inorder(start.right,traversal)
            traversal+=(str(start.value)+ "-")
        return traversal

tree= BinaryTree(1)
tree.root.left=node(2)
tree.root.right=node(3)
tree.root.left.left=node(4)
tree.root.left.right= node(5)
tree.root.right.left=node(6)
tree.root.right.right=node(7)
# tree.root.right.right.right=node(8)
print("Preorder")
print(tree.print_tree("preorder"))
print("Inorder")
print(tree.print_tree("inorder"))
print("Postorder")
print(tree.print_tree("postorder"))
