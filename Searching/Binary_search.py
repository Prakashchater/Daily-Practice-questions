#Recursive way
# def binary(arr,target,left, right):
#     if right >= 1:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             return binary(arr,target,left,mid-1)
#         else:
#             return binary(arr,target,mid+1,right)
#     else:
#         return -1

#Iterative Way

def binary(arr,target,left, right):
    if right >= 1:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
            return right
        else:
            left = mid + 1
            return left
    else:
        return -1

if __name__ == '__main__':
    arr = [10,20,30,40,50]
    target = 10
    print(binary(arr,target,0,len(arr)-1))
