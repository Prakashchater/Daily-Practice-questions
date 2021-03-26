def sorted(arr):
    currentidx = 0
    while currentidx < len (arr) - 1:
        small = currentidx
        for i in range(currentidx + 1, len(arr)):
            if arr[small] > arr[i]:
                small = i
        swap(currentidx,small,arr)
        currentidx = currentidx + 1
    return arr
def swap(i,j,arr):
    arr[i],arr[j]=arr[j],arr[i]

arr = [12,45,22,10,9,0,13]
print(sorted(arr))