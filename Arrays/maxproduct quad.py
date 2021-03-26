import sys
def maxproductquad(arr,n):
    if (n<4):
        return -1
    max_product= -sys.maxsize
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    max_product=max(max_product,arr[i]*arr[j]*arr[k]*arr[l])
    return max_product

arr=[1, -2, -3, 0, 7, -8, -2]
n=len(arr)
max=maxproductquad(arr,n)

if max ==-1:
    print("Invalid input")
else:
    print("max product is:",max)


