def Kthsorted(arr,k):

    arr.sort()

    return arr[k-1]

if __name__ == '__main__':
    arr = [7, 10, 4, 3, 20, 15]
    k=int(input())
    print(Kthsorted(arr,k))
