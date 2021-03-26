# def large1(arr):
#     mx = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > mx:
#             mx = arr[i]
#     return mx
#
# if __name__ == '__main__':
#     arr = [70, 11, 20, 4, 100]
#     print(large1(arr))


# def large2(arr):
#     mx = max(arr[0], arr[1])
#     secmx = min(arr[0],arr[1])
#
#     for i in range(2,len(arr)):
#         if arr[i]>mx:
#             secmx = mx
#             mx = arr[i]
#         elif arr[i] > secmx and mx != arr:
#             secmx = arr[i]
#     return secmx
#
# if __name__ == '__main__':
#     arr = [70, 11, 20, 4, 100]
#     print(large2(arr))

import sys
def large3(arr):
    if len(arr) < 3:
        print("Invalid")
        return
    first = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > first:
            first = arr[i]

    second = -sys.maxsize
    for i in range(0,len(arr)):
        if arr[i] > second and arr[i] < first:
            second = arr[i]

    third = -sys.maxsize
    for i in range(0,len(arr)):
        if arr[i] > third and arr[i] < second:
            third = arr[i]
    return third

if __name__ == '__main__':
    arr = [70, 11, 20, 4, 90,100]
    print(large3(arr))
