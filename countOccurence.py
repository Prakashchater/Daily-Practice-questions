def occurence(arr):
    count = 0
    for i in arr:
        if i == x:
            count +=1
    return count
if __name__ == '__main__':
    arr = [15, 6, 7, 10, 12, 20, 10, 28, 10]
    x = 10
    print(occurence(arr))
