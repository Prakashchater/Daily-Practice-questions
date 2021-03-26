def zerosones(arr,n):
    right=n-1
    left=0
    while(left<right):
        while(arr[left]==0 and left<right):
            left+=1
        while(arr[right]==1 and left<right):
            right-=1

        if(left<right):
            arr[left]=0
            arr[right]=1
            left=left+1
            right=right-1
    return arr

arr=[0,1,0,1,1,0,0,1]
n=len(arr)
print("Array after segregation")
print(zerosones(arr,n))







# if __name__ == '__main__':
