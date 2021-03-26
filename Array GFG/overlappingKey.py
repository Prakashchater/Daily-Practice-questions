def overlapping(arr,x,key,n):
    i = 0
    while i < n:
        j = 0
        while j < key:
            if arr[i + j] == x:
                break
            j = j + 1

        if j == key:
            return False
        i = i + key

        if i == n:
            return True
        j = i - key

        while j < n:
            if arr[j] == x:
                break
            j = j + 1

            if j == n:
                return False
            return True

if __name__ == '__main__':
    arr = [21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
    n = len(arr)
    x = int(input("Enter The number of segments you want to make: "))
    key = int(input("Enter the number you want to search: "))
    if overlapping(arr,x,key,n):
        print("Yes")
    else:
        print("No")




