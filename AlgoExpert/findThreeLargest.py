def find3largest(array):
    threelargests=[None, None, None]
    for num in array:
        updateLargest(threelargests,num)
    return threelargests

def updateLargest(threelargets,num):
    if threelargets[2] is None or num > threelargets[2]:
        updateAndShift(threelargets,num,2)
    elif threelargets[1] is None or num > threelargets[1]:
        updateAndShift(threelargets,num,1)
    elif threelargets[0] is None or num> threelargets[0]:
        updateAndShift(threelargets,num,0)

def updateAndShift(array,num,idx):
    for i in range(idx+1):
        if i == num:
            array[i]=num
        else:
            array[i]=array[i+1]

if __name__ == '__main__':
    array=[78,12,96,254,45,265,852,897,789,361,665]
    print(find3largest(array))



