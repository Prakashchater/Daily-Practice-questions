# Time complexity is O(N)
# Space complexity is O(1)
def subarraysum(arr,n,sum):
    currentsum=arr[0]
    start=0
    i=1
    while (i<=n):

        while (currentsum>sum) & (start<i+1):
            currentsum=currentsum-arr[start]
            start=start+1
        if currentsum==sum:
            print("The start index is",start,"and ends with index", i-1)
            return 1

        if (i<n):
            currentsum=currentsum+arr[i]
        i+=1

    print("No subarray present")
    return 0


arr=[1,4,20,3,10,5]
n=len(arr)
sum=33
subarraysum(arr,n,sum)



