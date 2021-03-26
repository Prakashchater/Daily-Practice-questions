#0(2^N) Time / O(N) space
# def nthfibo(n):
#     if n==2:
#         return 1
#     if n==1:
#         return 0
#     else:
#         return nthfibo(n-1)+nthfibo(n-2)

#O(N) time / O(n) space
# def nthfibo(n, memomize= {1: 0 , 2: 1}):
#     if n in memomize:
#         return memomize[n]
#     else:
#         memomize[n]=nthfibo(n-1,memomize)+nthfibo(n-2,memomize)
#     return memomize[n]

def nthfibo(n):
    lastTwo=[0,1]
    counter=3
    while counter <=n:
        nextfib=lastTwo[0]+lastTwo[1]
        lastTwo[0]=lastTwo[1]
        lastTwo[1]=l=nextfib
        counter+=1
    return lastTwo[1] if n>1 else lastTwo[0]

n=int(input())
print(nthfibo(n))

