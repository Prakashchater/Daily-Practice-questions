def kthSmallest(arr, n, k):
    # Sort the given array
    arr.sort()

    # Return k'th element in the
    # sorted array
    return arr[k - 1]


# Driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print("K'th smallest element is",
          kthSmallest(arr, n, k))

# This code is contributed by
# Shrikant13




