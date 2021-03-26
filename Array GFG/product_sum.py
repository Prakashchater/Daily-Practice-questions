# def productSum(arr, multiplier=1):
#     count = 0
#     for element in arr:
#         if type(element) is list:
#             count += productSum(element, multiplier + 1)
#         else:
#             count += element
#     return count * multiplier
#
# if __name__ == '__main__':
#     # arr = [5,2,[7,-1],3,[6,[-13,8],4]]
#     arr = [1,3,4]
#     print(productSum(arr))

# --------- Time - O(N^2) || Space - O(1) --------
"""
def productSum(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            count = count + arr[i]*arr[j]
    return count

if __name__ == '__main__':
    arr = [1,3,4]
    print(productSum(arr))
"""

def productSum(arr):
    array_sum = 0
    for i in range(0,len(arr),1):
        array_sum+= arr[i]

    square_array_sum = array_sum * array_sum

    individual_sum_square = 0
    for i in range(0,len(arr),1):
        individual_sum_square += arr[i]*arr[i]

    return int((square_array_sum - individual_sum_square)/2)

if __name__ == '__main__':
    arr = [1,3,4,4]
    print(productSum(arr))