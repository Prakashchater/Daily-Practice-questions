# TIME COMPLEXITY = O(N) || SPACE = O(1)
# def arr0s1s2s(arr):
#     arr0 = 0
#     arr1 = 0
#     arr2 = 0
#     for i in range(0,len(arr)):
#         if arr[i] == 0:
#             arr0+=1
#         if arr[i] == 1:
#             arr1+=1
#         if arr[i] == 2:
#             arr2+=1
#
#     for i in range(0,arr0):
#         arr[i] = 0
#     for i in range(arr0,(arr0 + arr1)):
#         arr[i] = 1
#     for i in range((arr0 + arr1),len(arr)):
#         arr[i] = 2
#     return arr

# def printarr(arr):
#     for i in range(0,len(arr)):
#         print(arr[i],end=" ")
#     print()
#
# if __name__ == '__main__':
#     arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
#     n = len(arr)
#     print(arr0s1s2s(arr))



# def arr0s1s2s(arr):
#     left = 0
#     right = len(arr) - 1
#     mid = 0
#     while mid <= right:
#         if arr[mid] == 0:
#             arr[left],arr[mid] = arr[mid],arr[left]
#             left+=1
#             mid+=1
#         elif arr[mid] == 1:
#             mid+=1
#         else:
#             arr[mid], arr[right] = arr[right], arr[mid]
#             right-=1
#     return arr
#
# if __name__ == '__main__':
#     arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
#     print(arr0s1s2s(arr))


