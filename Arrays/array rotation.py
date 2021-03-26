# O(N^2)      Time

arr=[1,2,3,4,5,6,7]
shift=int(input("no of times: "))
def rotation(arr):
    for i in range(0,len(arr)):
        print(arr[i],end=" ")
def rotationshift(arr,shift):
    for i in range(0,shift):
        temp=arr[0]
        for j in range(0,len(arr)-1):
            arr[j]=arr[j+1]
        arr[len(arr)-1]=temp
    return arr
print("Array before rotation:")
rotation(arr)
print()
rotatedarray=rotationshift(arr,shift)
print("Array after rotation:")
rotation(rotatedarray)


