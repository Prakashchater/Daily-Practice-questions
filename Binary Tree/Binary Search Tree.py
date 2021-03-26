# class BST:
#     def __init__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None
#
#     def inorder(self,root):
#         if root is not None:
#             self.inorder(root.left)
#             print(root.value)
#             self.inorder(root.right)
#
#     #Average: O(log(n)) time | O(1) space
#     #aworst: O(N) time | O(1) space
#     def insert(self,value):
#         currentNode=self
#         while True:
#             if value < currentNode.value:
#                 if currentNode.left is None:
#                     currentNode.left= BST(value)
#                     break
#                 else:
#                     currentNode=currentNode.left
#             else:
#                 if currentNode.right is None:
#                     currentNode.right=BST(value)
#                     break
#                 else:
#                     currentNode= currentNode.right
#         return self
#
#     #Average: O(log(n)) time | O(1) space
#     #aworst: O(N) time | O(1) space
#     def contain(self,value):
#         currentNode=self
#         while currentNode is not None:
#             if value < currentNode.value:
#                 currentNode=currentNode.left
#             elif value>currentNode.value:
#                 currentNode=currentNode.right
#             else:
#                 return True
#         return False
#
#
#     #Average: O(log(n)) time | O(1) space
#     #aworst: O(N) time | O(1) space
#     def remove(self,value,parentNode):
#         currentNode=self
#         while currentNode is not None:
#             if value < currentNode.value:
#                 parentNode=currentNode
#                 currentNode=currentNode.left
#             elif value < currentNode.value:
#                 parentNode=currentNode
#                 currentNode=currentNode.right
#             else:
#                 if currentNode.left is not None and currentNode.right is not None:
#                     currentNode.value=currentNode.right.getminValue()
#                     currentNode.right.remove(currentNode,currentNode)
#                 elif parentNode is None:
#                     if currentNode.left is not None:
#                         currentNode.value=currentNode.left.value
#                         currentNode.right=currentNode.left.right
#                         currentNode.left=currentNode.left.left
#                     elif currentNode.right is not None:
#                         currentNode.value=currentNode.right.value
#                         currentNode.left=currentNode.right.left
#                         currentNode.right=currentNode.right.right
#                     else:
#                         currentNode.value=None
#                 elif parentNode.left == currentNode:
#                     parentNode.left=currentNode.left if currentNode.left is not None else currentNode.right
#                 elif parentNode.right == currentNode:
#                     parentNode.right=currentNode.left if currentNode.left is not None else currentNode.right
#                 break
#         return self
#     def getminValue(self):
#         currentNode=self
#         while currentNode.left is not None:
#             currentNode=currentNode.left
#             return currentNode.value

# class BST:
#     def __init__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None
#
#     def inorder(self,root):
#         if root:
#             self.inorder(root.left)
#             print(root.value)
#             self.inorder(root.right)
#
#     def insert(self,value):
#         currentNode=self
#         while True:
#             if value < currentNode.value:
#                 if currentNode.left is None:
#                     currentNode.left=BST(value)
#                     break
#                 else:
#                     currentNode=currentNode.left
#             else:
#                 if value > currentNode.value:
#                     if currentNode.right is None:
#                         currentNode.right=BST(value)
#                         break
#                     else:
#                         currentNode=currentNode.right
#         return self
#
# r=BST(40)
# r=insert(r,30)
# r=insert(r,90)
# r=insert(r,70)
# r=insert(r,20)
# r=insert(r,10)
#
# print(inorder(r))

# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert
# a new node with the given key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

# A utility function to do inorder tree traversal


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
# 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20) 
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
inorder(r)




















