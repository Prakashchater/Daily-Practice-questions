# def duplicate(arr,n):
#     print("The repeating elements are: ")
#     for i in range (0,n):
#         if arr[abs(arr[i])]>=0:
#             arr[abs(arr[i])]=-arr[abs(arr[i])]
#         else:
#             print(abs(arr[i]),end=" ")
# if __name__ == '__main__':
#     arr=[1,2,3,4,1,5,6,2]
#     n=len(arr)
#     duplicate(arr,n)


arr1=[1,3,5,7,9,19]
arr2=[2,4,6,8,10,12,18]
arr=arr1+arr2
# print(arr)
arr.sort()
print(arr)


