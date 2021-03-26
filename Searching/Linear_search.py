# Time Complexity : O(N)

def linear(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

if __name__ == '__main__':
    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    x = int(input("Enter the number:"))
    print(linear(arr,x))
