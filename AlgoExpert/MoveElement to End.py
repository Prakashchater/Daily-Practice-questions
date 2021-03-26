# O(n) time amd O(1) space
# def moveElementToEnd(array,toMove):
#     i=0
#     j=len(array)-1
#     while i<j:
#         while i<j and array[j]==toMove:
#             j-=1
#         if array[i]==toMove:
#             array[i],array[j]=array[j],array[i]
#         i+=1
#     return array

# if __name__ == '__main__':
#     array=[4,1,3,2,2,5,2,2,2]
#     toMove=2
#     print(moveElementToEnd(array,toMove))

def movetoend(array,key):
    i=0
    j=len(array)-1
    while i<j:
        while i<j and array[j]==toMove:
            j-=1
        if array[i]== toMove:
            array[i],array[j]=array[j],array[i]
        i+=1
    return array

if __name__ == '__main__':
    array=[4,1,3,2,2,5,2,2,2]
    toMove=5
    print(movetoend(array,toMove))

