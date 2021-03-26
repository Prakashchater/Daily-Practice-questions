#O(logN) Time     ||     O(1) Space by using binary search

def searchinrotandsort(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=target<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
target = 10
i = searchinrotandsort(arr,target)
if i != -1:
    print ("Index: % d"% i)
else:
    print ("Key not found")


