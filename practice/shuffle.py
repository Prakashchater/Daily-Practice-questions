def shuffle(arr,n):
    res = [0]*(2*n)
    for i in range(n):
        res[2*i] = arr[i]
        res[(2*i)+1] = arr[n+i]
    return res
if __name__ == '__main__':
    arr = [2,5,1,3,4,7]
    n = 3
    print(shuffle(arr,n))