from collections import Counter
n=[2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
print("Initial array: ",n)
result=sorted(n,key=n.count,reverse=True)
print("Sorted element by frequency:" +str(result))