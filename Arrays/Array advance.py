def arrayAdvance(arr):
    fur_reach=0
    last=len(arr)-1
    i=0
    while i <= fur_reach and fur_reach < last:
        fur_reach=max(fur_reach,arr[i]+i)
        i+=1
    return fur_reach >= last

# arr=[3,3,1,0,2,0,1]
arr=[3,2,0,0,2,0,1]
print(arrayAdvance(arr))
