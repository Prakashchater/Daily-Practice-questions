# Time complexity is O(N)
# Auxiliary Space: O(1)

# def bubblesort(nums):
#     for i in range(len(nums)):
#         swapped=False
#         for j in range(0,len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#                 swapped=True
#         if swapped==False:
#             break
#
#
# nums=[5,3,8,6,7,2]
# bubblesort(nums)
# print(nums)


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0 , len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
if __name__ == '__main__':
    arr=[5,3,8,6,7,2]
    print(bubblesort(arr))

