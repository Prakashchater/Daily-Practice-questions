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

def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            swap(j,j-1,arr)
            j-=1
    return arr
def swap(i,j,arr):
    arr[i],arr[j] = arr[j],arr[i]

if __name__ == '__main__':
    arr = [12,13,1,2,15,6,8,9]
    print(insertionSort(arr))



