# Avg: O(log(n)) time | O(log(n)) space
#Worst: O(N) time | O(N) Space
# def closestValue(tree,target):
#     return closestValuehelper(tree,target,float("inf"))
#
# def closestValuehelper(tree,target,closest):
#     if tree is None:
#         return closest
#     if abs(target-closest) > abs(target-tree.value):
#         closest=tree.value
#     if target < tree.value:
#         return closestValuehelper(tree.left,target,closest)
#     if target > tree.value:
#         return closestValuehelper(tree.right,target,closest)
#     else:
#         return closest

# Avg: O(log(n)) time | O(1) space
#Worst: O(N) time | O(1) Space
def closestValue(tree,target):
    return closestValuehelper(tree,target,float("inf"))

def closestValuehelper(tree,target,closest):
    current=tree
    while current is not None:
        if abs(target-closest)> abs(target-current.value):
            closest=current.value
        if target < current.value:
            current=current.left
        elif target > current.value:
            current=current.right
        else:
            break
    return closest


