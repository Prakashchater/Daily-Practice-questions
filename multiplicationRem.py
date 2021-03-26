# def multi(arr,n):
#     m = 1
#     for i in arr:
#         m *= (i % n)
#     return m % n
#
# if __name__ == '__main__':
#     arr = [100, 10, 5, 25, 35, 14]
#     n = 11
#     print(multi(arr,n))
#

# def max_ones(arr):
#     c = 0
#     max_count = 0
#     i = 0
#     while i <= len(arr)-1:
#         if arr[i] == 0:
#             max_count = max(max_count,c)
#             c = 0
#         else:
#             c += 1
#         i+=1
#     return  max(max_count,c)
#
# arr = [0,0,0,0,0,1]
# print(max_ones(arr))




