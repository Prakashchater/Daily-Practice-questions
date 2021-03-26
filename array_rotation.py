# def left_rotation(arr,k):
#     temp = []
#     i = 0
#     while i < k:
#         temp.append(arr[i])
#         i += 1
#
#     i = 0
#     while k < len(arr):
#         arr[i] = arr[k]
#         i += 1
#         k += 1
#     arr[:] = arr[:i] + temp
#     return arr
#
# if __name__ == '__main__':
#     arr = [1,2,3,4,5,6,7]
#     k = 2
#     print(left_rotation(arr,k))

# def right_rotation(arr,k):
#     temp = []
#     for i in range(len(arr)-k,len(arr)):
#         temp.append(arr[i])
#
#     for i in range(0,len(arr)-k):
#         temp.append(arr[i])
#
#     return temp
#
# arr = [1,2,3,4,5,6,7]
# k = 3
# print(len(arr))
# print(right_rotation(arr,k))

arr = [3,1,2]
k = 1
temp = []
for i in range(k,len(arr)):
    temp.append(arr[i])

for i in range(0,k):
    temp.append(arr[i])
print(temp)
