class binarytree:
    def __init__(self,value):
        self.value=value
        self.right= None
        self.left= None

def branchsum(root):
        sum=[]
        calculatebranchsum(root,0,sum)
        return sum

def calculatebranchsum(node,runningsum,sum):
    if node is None:
        return
    newrunningsum = runningsum+node.value
    if node.left is None and node.right is None:
        sum.append(newrunningsum)
        return

    calculatebranchsum(node.left,newrunningsum,sum)
    calculatebranchsum(node.right,newrunningsum,sum)

