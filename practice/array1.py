# array = [1,2,3,4,5,6,7,8,9,10,11,12]
# key = 4

# def dummy(array, key):
#   sub_arr_size = len(array) // key

#   sub_array_list = [[0]*sub_arr_size for i in range(key)]
#   idx = 0
#   pos = 0
# #   print(sub_array_list)

#   for i in range(len(array)):
#     if idx >= sub_arr_size:
#       pos += 1
#       idx = 0
#     sub_array_list[pos][idx] = array[i]
#     idx+=1

#   print(sub_array_list)


# dummy(array, key) 

def subarray(arr,k,x):
    # my_list = [arr[i:i+k] for i in range(0, len(arr),k)]
    # print(my_list)
    for i in range(0,len(arr),k):
        l = arr[i:i+k]
            

arr = [ 21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
k = 5
x = 21

subarray(arr,k)
