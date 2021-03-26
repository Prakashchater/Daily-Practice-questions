# def kadaneAlgorithm(array):
#     maxEnding=array[0]
#     maxsoFar=array[0]
#     for num in array[1:]:
#         maxEnding=max(num, maxEnding+num)
#         maxsoFar= max(maxsoFar,maxEnding)
#     return maxsoFar
#
# if __name__ == '__main__':
#     array= [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
#     print(kadaneAlgorithm(array))
#
