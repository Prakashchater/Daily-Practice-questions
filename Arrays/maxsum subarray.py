def maxsumarray(arr):
    size=len(arr)
    curr_sum=0
    max_sum=arr[0]
    start,end,pointer=0,0,0
    for i in range(0,size):

        curr_sum=curr_sum+arr[i]
        if(max_sum<curr_sum):
            start=pointer
            end=i
            max_sum=curr_sum

        if(curr_sum<0):
            curr_sum=0
            pointer=i+1

    print("Maximum sum array is",max_sum)

arr=[1, 12, -5, -6, 50, 3]
maxsumarray(arr)
