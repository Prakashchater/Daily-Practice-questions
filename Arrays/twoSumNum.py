# O(n^2) time | O(1) space

# def twosumarray(arr,targetsum):
#     for i in range(len(arr)-1):
#         first=arr[i]
#         # print("1st",first,end=' ')
#         for j in range(i+1,len(arr)):
#             second=arr[j]
#             # print("2nd",second,end=' ')
#             if first+second==targetsum:
#                 return print([first,second])
#     return []
# arr=[3,5,-4,8,11,1,-1,6]
# targetsum=int(input())
# twosumarray(arr,targetsum)


#O(nlogn) time| O(1) space

# def twosumarray(arr,targetsum):
#     arr.sort()
#     left=0
#     right=len(arr)-1
#     while(left<right):   #
#         sum=arr[left]+arr[right]
#         if sum==targetsum:
#             return print([arr[left],arr[right]])
#         elif sum<targetsum:
#             left+=1
#         elif sum>targetsum:
#             right-=1
#     return []
# arr=[3,5,-4,8,11,1,-1,6]
# targetsum=int(input())
# twosumarray(arr,targetsum)
"""
def twosumarray(arr,targetsum):
    nums={}
    for num in arr:
        potsum=targetsum-num
        if potsum in nums:
            return print([potsum,num])
        else:
            nums[num]=True
    return []
arr=[3,5,-4,8,11,1,-1,6]
targetsum=int(input())
twosumarray(arr,targetsum)
"""

def sumnum(arr,target):
    arr.sort()
    l=0
    h=len(arr)-1
    while (l<=h):
        # sum=arr[l]+arr[h]
        if (arr[l]+arr[h]<target):
            l=l+1
        elif (arr[l]+arr[h]>target):
            h=h-1
        elif (arr[l]+arr[h]==target):
            print("Values of the pair: ",arr[l], "&", arr[h])
            h = h - 1
            l = l + 1

arr=[1, -2, 1, 0, 5]
target=99
sumnum(arr,target)






