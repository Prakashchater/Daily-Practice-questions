"""
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Function to push node at head
def push(head, data):
	if not head:
		return Node(data)
	temp = Node(data)
	temp.next = head
	head = temp
	return head

# Function to remove the last node
# of the linked list
def removeLastNode(head):
	if head == None:
		return None
	if head.next == None:
		head = None
		return None
	second_last = head
	while(second_last.next.next):
		second_last = second_last.next
	second_last.next = None
	return head

# Driver code
if __name__=='__main__':

	# Start with the empty list
	head = None
	# Use push() function to con
	# the below list 8 . 23 . 11 . 29 . 12
	head = push(head, 12)
	head = push(head, 29)
	head = push(head, 11)
	head = push(head, 23)
	head = push(head, 8)

	head = removeLastNode(head)
	while(head):
		print("{} ".format(head.data), end ="")
		head = head.next

# This code is contributed by Vikash kumar 37
"""
# import sys
# import math
#
# class node:
# 	def __init__(self,data):
# 		self.data=data
# 		self.next=None
# 	def push(head,data):
# 		if not head:
# 			return node(data)
# 		temp=node(data)
# 		temp.next= head
# 		head=temp
# 		return head
#
# 	def removelastNode(head):
# 		if head==None:
# 			return None
# 		if head.next==None:
# 			head=None
# 			return None
# 		sec_last=head
# 		while(sec_last.next.next):
# 			sec_last=sec_last.next
# 		sec_last.next=None
# 		return head
# 	if __name__ == '__main__':
# 	    head=None
# 		head=push(head, 12)
# 		head=push(head, 15)
# 		head=push(head, 16)
# 		head=push(head, 17)
# 		head=push(head, 18)
# 		head=removelastNode(head)
# 		while(head):
# 			print("{}".format(head.data),end=" ")
# 			head=head.next







