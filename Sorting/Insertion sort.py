# def insertionsort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key
#     return arr
#
# if __name__ == '__main__':
#     arr = [12,13,1,2,15,6,8,9]
#     print(insertionsort(arr))

# --------- Algoexpert method -----------

# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         j = i
#         while j > 0 and arr[j] < arr[j-1]:
#             swap(j,j-1,arr)
#             j-=1
#     return arr
# def swap(i,j,arr):
#     arr[i],arr[j] = arr[j],arr[i]
#
# if __name__ == '__main__':
#     arr = [12,13,1,2,15,6,8,9]
#     print(insertionSort(arr))


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         curr_ele = arr[i]
#         pos = i
#         while curr_ele < arr[pos - 1] and pos > 0:
#             arr[pos] = arr[pos - 1]
#             pos = pos - 1
#         arr[pos] = curr_ele
#
#
# if __name__ == '__main__':
#     arr = [5,1,3,2,4]
#     insertion_sort(arr)
#     print(arr)



##DECENDING ORDER
def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr_ele = arr[i]
        pos = i
        while curr_ele > arr[pos - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = curr_ele


if __name__ == '__main__':
    arr = [5,1,3,2,4]
    insertion_sort(arr)
    print(arr)








