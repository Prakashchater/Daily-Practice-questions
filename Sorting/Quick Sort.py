"""
def pivot_place(list1,first_idx,last_idx):
    pivot=list1[first_idx]
    left_idx=first_idx+1
    right_idx=last_idx
    while True:
        while left_idx<=right_idx and list1[left_idx]<=pivot:
            left_idx=left_idx+1
        while left_idx<=right_idx and list1[right_idx>=pivot]:
            right_idx=right_idx-1
        if right_idx<left_idx:
            break
        else:
            list1[left_idx],list1[right_idx]=list1[right_idx],list1[left_idx]
    list1[first_idx], list1[right_idx] = list1[right_idx], list1[first_idx]
    return right_idx

def quicksort(list1,first_idx,last_idx):
    if first_idx<last_idx:
        p=pivot_place(list1,first_idx,last_idx)
        quicksort(list1,first_idx,p-1)   #solving recursively
        quicksort(list1,p+1,last_idx)

list1=[56,26,93,17,31,44]
n=len(list1)
quicksort(list1,0,n-1)
print("the quick sort is:",list1)
"""

# Python program for implementation of Quicksort Sort

# # This function takes last element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot
# def partition(arr,low,high):
# 	i = ( low-1 )		# index of smaller element
# 	pivot = arr[high]	 # pivot
#
# 	for j in range(low , high):
#
# 		# If current element is smaller than the pivot
# 		if arr[j] < pivot:
#
# 			# increment index of smaller element
# 			i = i+1
# 			arr[i],arr[j] = arr[j],arr[i]
#
# 	arr[i+1],arr[high] = arr[high],arr[i+1]
# 	return ( i+1 )
#
# # The main function that implements QuickSort
# # arr[] --> Array to be sorted,
# # low --> Starting index,
# # high --> Ending index
#
# # Function to do Quick sort
# def quickSort(arr,low,high):
# 	if low < high:
#
# 		# pi is partitioning index, arr[p] is now
# 		# at right place
# 		pi = partition(arr,low,high)
#
# 		# Separately sort elements before
# 		# partition and after partition
# 		quickSort(arr, low, pi-1)
# 		quickSort(arr, pi+1, high)
#
# # Driver code to test above
# arr = [10,80,30,90,40,50,70]
# n = len(arr)
# quickSort(arr,0,n-1)
# print ("Sorted array is:")
# for i in range(n):
# 	print ("%d" %arr[i],end=" "),


# def pivot_ele(list1, first, last):
#     pivot = list1[first]
#     left = first + 1
#     right = last
#
#     while True:
#         while left <= right and list1[left] <= pivot:
#             left = left + 1
#         while left <= right and list1[right] >= pivot:
#             right = right - 1
#
#         if left > right:
#             break
#         else:
#             list1[left], list1[right] = list1[right], list1[left]
#     list1[first], list1[right] = list1[right], list1[first]
#     return right
#
#
# def quick_sort(list1, first, last):
#     if first < last:
#         p = pivot_ele(list1, first, last)
#         #Left sublist
#         quick_sort(list1, first, p-1)
#         #Right Sublist
#         quick_sort(list1, p+1, last)
#
# if __name__ == '__main__':
#     list1 = [56, 26, 93, 17, 31, 44]
#     n = len(list1)
#     quick_sort(list1, 0, n-1)
#     print(list1)


def pivot_ele(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last

    while True:
        while left <= right and list1[left] >= pivot:
            left = left + 1
        while left <= right and list1[right] <= pivot:
            right = right - 1

        if left > right:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right


def quick_sort(list1, first, last):
    if first < last:
        p = pivot_ele(list1, first, last)
        #Left sublist
        quick_sort(list1, first, p-1)
        #Right Sublist
        quick_sort(list1, p+1, last)

if __name__ == '__main__':
    list1 = [56, 26, 93, 17, 31, 44]
    n = len(list1)
    quick_sort(list1, 0, n-1)
    print(list1)

