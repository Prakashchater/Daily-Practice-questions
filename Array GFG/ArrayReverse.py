def reverseWord(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr
if __name__ == '__main__':
    arr = [2,1,3,4]
    start = 0
    end = len(arr) - 1
    print(reverseWord(arr,start,end))