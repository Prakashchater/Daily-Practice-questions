#O(N) Time  ||  O(1) Space

def missing(arr):
    n=len(arr)
    total=(n+1)*(n+2)/2
    sum_of_array=sum(arr)
    return int(total-sum_of_array)

arr=[1,2,3,5,6]
miss=missing(arr)
print(miss)
