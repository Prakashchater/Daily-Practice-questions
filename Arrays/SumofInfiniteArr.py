def func(sumArray, x, n):

    mod = 10 ** 9 + 7

    # Number of times the given array comes completely upto index x.
    count = (x // n) % mod

    res = (count * sumArray[n]) % mod

    # Adding the remaining elements sum.
    res = (res + sumArray[(x % n)]) % mod

    return res


'''
    Time Complexity:O(Q*(R-L))
    Space Complexity:O(1).
    Where Q is the number of given queries, and L and R are the give
'''


def sumInRanges(arr, n, queries, q):
    mod = 10 ** 9 + 7

    #  It stores answer for each query.
    ans = []

    # Traversing the given queries
    for ranges in queries:
        # Substract 1 from both L and R to use it as 0-based indexing
        l = ranges[0] - 1
        r = ranges[1] - 1

        # It stores the sum
        sume = 0

        for i in range(l, r + 1):
            index = (i % n)
            sume = (sume + arr[index]) % mod

        sume %= mod
        # Add answer to each query
        ans.append(sume)

    return ans


# def sumInRanges(arr, n, queries, q):
#     mod = 10 ** 9 + 7
#
#     #  It stores answer for each query.
#     ans = []
#
#     # It store cumulative sum where sumArray[i] = sum(A[0]+..A[i]).
#     sumArray = [0 for i in range(n + 1)]
#
#     for i in range(1, n + 1):
#         sumArray[i] = (sumArray[i - 1] + arr[i - 1]) % mod
#
#     # Traversing the given queries.
#     for ranges in queries:
#
#         l = ranges[0]
#         r = ranges[1]
#
#         #  It stores the prefix sum from index 0 to index r in an infinite array.
#         rsum = func(sumArray, r, n)
#
#         # It stores the prefix sum from index 0 to index l-1 in an infinite array.
#         lsum = func(sumArray, l - 1, n)
#
#         # Add answer for each query.
#         ans.append((rsum - lsum + mod) % mod)
#
#     return ans