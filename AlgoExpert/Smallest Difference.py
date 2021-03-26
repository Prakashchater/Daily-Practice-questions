# O(nlog(n)+mlog(m)) time || O(1) space
# def smallestdifference(array1,array2):
#     array1.sort()
#     array2.sort()
#     idx1=0
#     idx2=0
#     smallest=float("inf")
#     current=float("inf")
#     smallestPair=[]
#     while idx1<len(array1) and idx2<len(array2):
#         firstnum=array1[idx1]
#         secondnum=array2[idx2]
#         if firstnum < secondnum:
#             current= secondnum-firstnum
#             idx1+=1
#         elif secondnum<firstnum:
#             current=firstnum-secondnum
#             idx2+=1
#         else:
#             return [firstnum , secondnum]
#         if smallest > current:
#             smallest=current
#             smallestPair=[firstnum,secondnum]
#     return smallestPair
#
# if __name__ == '__main__':
#     array1=[-1,3,5,10,20,28,3]
#     array2=[26,134,135,13,17]
#     print(smallestdifference(array1,array2))


def smallestdifference(arr1,arr2):
    arr1.sort()
    arr2.sort()
    idx1=0
    idx2=0
    smallest=float("inf")
    current=float("inf")
    smallestpair=[]
    while idx1< len(arr1) and idx2 < len(arr2):
        firstnum=arr1[idx1]
        secondnum=arr2[idx2]
        if firstnum < secondnum:
            current=secondnum-firstnum
            idx1+=1
        elif secondnum<firstnum:
            current=firstnum - secondnum
            idx2+=1
        else:
            return [firstnum , secondnum]
        if current< smallest:
            smallest=current
            smallestpair=[firstnum,secondnum]
    return smallestpair

if __name__ == '__main__':
    array1=[-1,3,5,10,20,28,3]
    array2=[26,134,135,13,17]
    print(smallestdifference(array1,array2))