# def monotonics(arr):
#     n = len(arr)
#     for i in range(1,n):
#         if arr[i-1] >= arr[i]:
#             return True
#         else:
#             return False
#
# arr = [1,5,3,4]
# print(monotonics(arr))

# arr = [1,1,0,0,1,1,1]
# c = 0
# for i in range(len(arr)):
#     if arr[i] == 1:
#         c += 1
#     else:
#         c = 0
# print(c)

# arr = [12, 35, 9, 56, 24, 34]
# arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
# print(arr)

# def swap_pos(arr, pos1, pos2):
#
#     arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
#     return arr
#
# if __name__ == '__main__':
#     arr = [12, 35, 9, 56, 24, 34]
#     pos1 = 1
#     pos2 = 3
#     print(swap_pos(arr,pos1-1,pos2-1))

def reverseing(arr):
    start = 0
    end =len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr

if __name__ == '__main__':
    arr = [12, 35, 9, 56, 24, 34]
    print(reverseing(arr))
