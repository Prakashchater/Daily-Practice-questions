def cummilative(arr):
    l = []
    j = 0
    for i in range(len(arr)):
        j += arr[i]
        l.append(j)
    return l

if __name__ == '__main__':
    arr = [10,20,30,40,50]
    print(cummilative(arr))