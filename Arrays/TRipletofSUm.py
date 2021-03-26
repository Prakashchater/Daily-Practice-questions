# Time complexity is O(N)

def tripletsum(arr,n,sum):
    arr.sort()
    for i in range(0,n-2):
        l=i+1   # index of the first element in the remaining elements
        r=n-1    # index of the last element

        while(l<r):

            if(arr[i]+arr[l]+arr[r]==sum):
                print("Triplet is", arr[i],
                      ', ', arr[l], ', ', arr[r]);
                return True

            elif (arr[i]+arr[l]+arr[r]<sum):
                l=l+1
            else:
                r=r-1

    return False

arr=[1, 2, 3, 4, 5]
sum=9
n=len(arr)
tripletsum(arr,n,sum)
