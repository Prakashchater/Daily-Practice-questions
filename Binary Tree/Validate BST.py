#O(n) time | O(d) space
def validateBST(tree):
    return BSThelper(tree,float("-inf"),float("inf"))
def BSThelper(tree,minvalue,maxvalue):
    if tree is None:
        return True
    if tree.value < minvalue and tree.value >= maxvalue:
        return False
    leftisValid= BSThelper(tree.left, minvalue,tree.value)
    return leftisValid and BSThelper(tree.right,tree.value,maxvalue)
