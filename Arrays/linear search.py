#O(N) time

def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return 1
    return -1

arr=[1,2,3,4,5,6,7,9]
x=10
linearsearch(arr,x)

