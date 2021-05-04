# def mergeSort(list1):
#     # Checking if the list of number is less than 1
#     if len(list1) > 1:
#         mid = len(list1) // 2
#         left = list1[:mid]
#         right = list1[mid:]
#         mergeSort(left)
#         mergeSort(right)
#         i=0
#         j=0
#         k=0
#         # comparing the left list and right list
#         while i<len(left) and j < len(right):
#             if left[i] < right[j]:
#                 list1[k] = left[i]
#                 i = i+1
#                 k = k+1
#             else:
#                 list1[k] = right[j]
#                 j = j+1
#                 k = k+1
#         # If the list had left over an element then this loop will occur
#         while i < len(left):
#             list1[k] = left[i]
#             i = i+1
#             k = k+1
#         while j < len(right):
#             list1[k] = right[j]
#             j = j+1
#             k = k+1
#
# if __name__ == '__main__':
#     n = int(input("Enter the no. of element:"))
#     list1 = [int(input()) for x in range(n)]
#     mergeSort(list1)
#     print("Sorted list: ", list1)

def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left = list1[:mid]
        right = list1[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
                k += 1
            else:
                list1[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1

if __name__ == '__main__':
    n = int(input("Enter the no. of element:"))
    list1 = [int(input()) for x in range(n)]
    merge_sort(list1)
    print("Sorted list: ", list1)