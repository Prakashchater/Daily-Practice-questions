def maxmin(array,left,right):
    arr_max= left
    arr_min= left
    # array having only 1 number
    if left==right:
        arr_max=array[left]
        arr_min=array[left]
        return (arr_max,arr_min)
    # array having 2 numbers
    elif right==left+1:
        if array[left]>array[right]:
            arr_max=array[left]
            arr_min=array[right]
        else:
            arr_max=array[right]
            arr_min=array[left]
        return (arr_max,arr_min)
    # array having more than 2 number
    else:
        mid = int((left + right) / 2)
        arr_max1, arr_min1 = maxmin(array,left,mid)
        arr_max2, arr_min2 = maxmin(array,mid+1,right)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

if __name__ == '__main__':
    array=[]
    n=int(input("Enter the size of the array: "))
    left=0
    right=n-1
    print("Enter the numbers:")
    for i  in range(n):
        array.append(int(input()))
    arr_max, arr_min = maxmin(array,left,right)
    print("largest number: ", arr_max)
    print("Smallest number: ",arr_min)

