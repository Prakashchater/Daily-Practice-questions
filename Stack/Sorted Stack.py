# def sortedstack(s,element):
#     if len(s)==0 or element > s[-1]:
#         s.append(element)
#         return
#     else:
#         temp=s.pop()
#         sortedstack(s,element)
#         s.append(temp)
#
# def sortstack(s):
#     if len(s)!=0:
#         temp=s.pop()
#         sortstack(s)
#         sortedstack(s,temp)
#
# def printstack(s):
#     for i in s[::-1]:
#         print(i,end=" ")
#     print()
#
# if __name__ == '__main__':
#     s=[]
#     s.append(33)
#     s.append(21)
#     s.append(-7)
#     s.append(3)
#     s.append(9)
#     print("Stack elements before sorting: ")
#     printstack(s)
#
#     sortstack(s)
#
#     print("\nStack elements after sorting: ")
#     printstack(s)

def insertstack(s,element):
    while len(s)==0 or element > s[-1]:
        s.append(element)
        return
    temp=s.pop()
    insertstack(s,element)
    s.append(temp)

def sortedstack(s):
    if len(s)!=0:
        temp=s.pop()
        sortedstack(s)
        insertstack(s,temp)

def printstack(s):
    for i in s[::-1]:
        print(i,end=" ")
    print()

if __name__ == '__main__':
    s=[]
    s.append(10)
    s.append(60)
    s.append(50)
    s.append(100)
    s.append(90)
    print("Elements before stack: ")
    printstack(s)

    sortedstack(s)

    print("Elements after stack: ")
    printstack(s)


