# Time Complexity: O(n2) as there are two nested loops.
# Auxiliary Space: O(1)

"""
def selectionsort(list1):
    for i in range(len(list1)): #Sorted list
        min_val=i
        for j in range(i+1,len(list1)):     #Unsorted list
            if list1[min_val]>list1[j]:
                min_val=j

        list1[i],list1[min_val]=list1[min_val],list1[i]



n=int(input("Enter the element in list:"))
list1=[int(input()) for x in range (n)]
selectionsort(list1)
print("Sorted list:",list1)
"""

# n=int(input("Enter the element in the list:"))
# list1=[int(input("Before sorting:")) for i in range(n)]
# min_val=min(list1)
# min_ind=list1.index(min_val)
# list1[0],list1[min_val]=list1[min_val],list1[0]
# print("After sorting:",list1)

# def selectionSort(arr):
#     curr_idx = 0
#     while curr_idx < len(arr) - 1 :
#         small = curr_idx
#         for i in range(curr_idx+1,len(arr)):
#             if arr[small] > arr[i]:
#                 small = i
#         arr[small] , arr[curr_idx] = arr[curr_idx],arr[small]
#         curr_idx+=1
#     return arr
#
# if __name__ == '__main__':
#     arr = [7,8,2,1,9,6,2]
#     print(selectionSort(arr))

# -------- ALgoExpert Method----------
# Time = O(N)
# Space = O(N)
def selectionSort(arr):
    curr_idx = 0
    while curr_idx < len(arr) - 1:
        small_ele = curr_idx
        for i in range(curr_idx + 1,len(arr)):
            if arr[small_ele] > arr[i]:
                small_ele = i
        swap(curr_idx,small_ele,arr)
        curr_idx+=1
    return arr

def swap(i,j,arr):
    arr[i],arr[j] = arr[j],arr[i]

if __name__ == '__main__':
    arr = [7,8,2,1,9,6,2]
    print(selectionSort(arr))










