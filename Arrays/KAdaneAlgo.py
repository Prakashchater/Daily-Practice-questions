# from sys import maxint
# def contagious(arr):
#     pos_contag=0        #positive contiguous segments of the array
#     max_sum_contag=-maxint-1           #maximum sum contiguous segment among all positive segments
#
#     for i in range(0,len(arr)):
#         pos_contag=pos_contag+arr[i]
#
#         if(max_sum_contag<pos_contag):
#             max_sum_contag=pos_contag
#         elif(pos_contag<0):
#             pos_contag=0
#
#     return max_sum_contag
#
# arr=[-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# print("The max contagious sum is: ",contagious(arr,len(arr)))

def kadane(arr):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0 :
            max_ending_here = 0
        elif max_so_far < max_ending_here :
            max_so_far = max_ending_here
    return max_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(arr))




