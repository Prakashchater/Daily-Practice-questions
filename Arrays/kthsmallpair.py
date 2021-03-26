import sys
def ksmallpairs(arr1,n1,arr2,n2,k):
    if(k>n1*n2):    #if k value is greater than the multiplied length of
                    #arr1 and arr2 then this condition will satisfy
        print("Invalid input")
        return
    index1=[0 for i in range (n1)]  #
    while(k>0):      # Initialize current pair sum as infinite
        min_index=0
        min_sum=sys.maxsize
        for i1 in range(0,n1,1):       #check if arr[1]+arr[2] gives minimum sum
            if(index1[i1]<n2 and arr1[i1]+arr2[index1[i1]]<min_sum):
                min_index=i1    #update index that gives minimum sum
                min_sum=arr1[i1]+arr2[index1[i1]]       #update minimum sum
        print("(",arr1[min_index],",",arr2[index1[min_index]],")")
        index1[min_index]+=i1
        k-=1

if __name__ == '__main__':
    arr1=[1,3]
    n1=len(arr1)

    arr2=[2]
    n2=len(arr2)

    k=4
    ksmallpairs(arr1,n1,arr2,n2,k)


