def merge_inversion(arr,n):
    inv_arr = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j] :
                inv_arr += 1
    return inv_arr
if __name__ == '__main__':
    arr=[1, 20, 6, 4, 5]
    n=len(arr)
    print(merge_inversion(arr,n))