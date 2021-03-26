def reversearray(array,start,end):
    if start>=end:
        return
    array[start],array[end]= array[end],array[start]
    reversearray(array,start+1,end-1)

if __name__ == '__main__':
    array=[]
    n=int(input("Enter the size of the array: "))
    for i in range(n+1):
        array.append(int(input("Enter the number: ")))
    print(array)
    reversearray(array,0,n)
    print(array)


