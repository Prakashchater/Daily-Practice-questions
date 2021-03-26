# # Loop through each element and maintains a count of majority element, and a majority index, maj_index
# # If the next element is same then increment the count if the next element is not same then decrement the count.
# # if the count reaches 0 then changes the maj_index to the current element and set the count again to 1.
# # Now again traverse through the array and find the count of majority element found.
# # If the count is greater than half the size of the array, print the element
# # Else print that there is no majority element
#
def match(arr):
    maj_index=0
    c=1
    for i in range(len(arr)):
        if arr[maj_index] ==arr[i]:
            c+=1
        else:
            c-=1
        if c==0:
            maj_index=i
            c=1
    return arr[maj_index]

def majority(arr,cand):
    c=0
    for i in range(len(arr)):
        if arr[i]==cand:
            c+=1
    if c >len(arr)/2:
        return True
    else:
        return False

def printmajority(arr):
    cand=match(arr)
    if majority(arr,cand)== True:
        print(cand)
    else:
        print("No majority element")

arr=[3, 3, 4, 2, 4, 4, 2, 4, 4]
printmajority(arr)


# def findMajority(arr, n):
#     maxCount = 0;
#     index = -1  # sentinels
#     for i in range(n):
#
#         count = 0
#         for j in range(n):
#
#             if (arr[i] == arr[j]):
#                 count += 1
#
#         # update maxCount if count of
#         # current element is greater
#         if (count > maxCount):
#             maxCount = count
#             index = i
#
#             # if maxCount is greater than n/2
#     # return the corresponding element
#     if (maxCount > n // 2):
#         print(arr[index])
#
#     else:
#         print("No Majority Element")
#
#     # Driver code
#
#
# if __name__ == "__main__":
#     arr = [3, 3, 4, 2, 4, 4, 2, 4]
#     n = len(arr)
#
#     # Function calling
#     findMajority(arr, n)