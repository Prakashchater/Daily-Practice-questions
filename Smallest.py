# def small1(arr):
#     min1 = arr[0]
#     for i in range(0,len(arr)):
#         if arr[i] < min1:
#             min1 = arr[i]
#     return min1
#
# if __name__ == '__main__':
#     arr = [20, 10, 20, 1, 100,-14]
#     print(small1(arr))


# def small2(arr):
#     first, second = float('inf'), float('inf')
#     for i in range(len(arr)):
#         if i <= first:
#             first, second = i, first
#         elif i < second:
#             second = i
#     return second

#
# if __name__ == '__main__':
#     arr = [20, 10, 20, 1, 1, 100, -14]
#     print(small2(arr))

def small3(arr):
    first, second,third = float('inf'), float('inf'), float('inf')
    for i in range(0,len(arr)):
        if arr[i] < first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] < second:
            third = second
            second = arr[i]
        elif arr[i] < third:
            third = arr[i]

    return third

if __name__ == '__main__':
    arr = [100,98,10,78,99,101]
    print(small3(arr))

