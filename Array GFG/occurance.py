def RepeatedArr(arr,x):
    count = 0
    for i in arr:
        if i == x:
            count+=1
    return count

if __name__ == '__main__':
    arr = [0, 5, 5, 5, 4]
    x = int(input())
    if x not in arr:
        print("Not present.")
    else:
        print(RepeatedArr(arr,x))

