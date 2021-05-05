def same(arr):
    l = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j] and arr[i] not in l:
                l.append(arr[i])
    return l

if __name__ == '__main__':
    arr = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
    print(same(arr))
