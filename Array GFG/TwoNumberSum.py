# ------- Time = O(N^2) || Space = O(1)---------
# def twoNumberSum(arr,target):
#     for i in range(len(arr)-1):
#         firstnum = arr[i]
#         for j in range(i+1,len(arr)):
#             second_num = arr[j]
#             if firstnum + second_num == target:
#                 return [firstnum,second_num]
#     return []
#
# if __name__ == '__main__':
#     arr = [9,2,3,6,-1,5,1,3]
#     target = 9
#     print(twoNumberSum(arr,target))


# ------ Time= O(log(N)) || Space - O(1) -----
def twoSumNumber(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left],arr[right]]
        elif current_sum > target :
            right -= 1
        elif current_sum < target:
            left+=1
    return []

if __name__ == '__main__':
    arr = [9,2,3,6,-1,5,1,3]
    target = 9
    print(twoSumNumber(arr,target))

