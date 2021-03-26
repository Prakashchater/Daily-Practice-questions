#O(1) time and O(N^2) space
def selectionsort(array):
    currentidx=0
    while currentidx<len(array)-1:
        nextidx=currentidx
        for i in range(currentidx+1,len(array)):
            if array[nextidx]>array[i]:
                nextidx=i
        swap(currentidx,nextidx,array)
        currentidx+=1
    return array
def swap(i,j,array):
    array[i],array[j]=array[j],array[i]

if __name__ == '__main__':
    array=[7,9,6,5,1,3]
    print(selectionsort(array))