import sys
def large3ele(arr,arr_size):
    # There should be atleast three
    # elements
    if (arr_size< 3):
        print(" Invalid Input ")
        return

    third = first = sec = -sys.maxsize

    for i in range(0,arr_size):
        if(arr[i]>first):
            third=sec
            sec=first
            first=arr[i]
        elif(arr[i]>sec):
            third=sec
            sec=arr[i]
        elif(arr[i]>first):
            first=arr[i]
    print("The largest 3 elements are: ", first,sec,third)


arr=[54,52,63,85,96,36,94,88,99,57]
n=len(arr)
large3ele(arr,n)