"""ITERATIVE"""
#O(n) time | O(N) space
# def invertBST(tree):
#     queue=[tree]
#     while len(queue):
#         current= queue.pop(0)
#         if current is None:
#             return
#         swapLeftandRight(current)
#         queue.append(current.left)
#         queue.append(current.right)
#
# def swapLeftandRight(tree):
#     tree.left,tree.right=tree.right,tree.left

"""RECURSIVE"""
#O(N) Time || O(d) space
def invertBinary(tree):
    if tree is None:
        return
    swapLeftandRight(tree)
    invertBinary(tree.left)
    invertBinary(tree.right)

def swapLeftandRight(tree):
    tree.left, tree.right=tree.right,tree.left