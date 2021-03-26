# def calculatestack(price,s):
#     n=len(price)
#     st=[]
#     st.append(0)
#     s[0]=1
#     for i in range(1,n):
#         while (len(st)> 0 and price[st[-1]] <= price[i]):
#             st.pop()
#         s[i]=i+1 if len(st) <=0 else (i-st[-1])
#         st.append(i)
#
# def printstack(arr,n):
#     for i in range(0,n):
#         print(arr[i],end=" ")
#
# price=[100,80,60,70,60,75,85]
# s=[0 for i in range(len(price)+1)]
#
# calculatestack(price,s)
#
# printstack(s,len(price))

def calculatestack(price,s):
    n=len(price)
    st=[]
    st.append(0)
    s[0]=1
    for i in range(1,n):
        while (len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()
        s[i]=i+1 if len(st) <=0 else (i-st[-1])
        st.append(i)

def printstack(arr,n):
    for i in range(0,n):
        print(arr[i],end=" ")
price=[100,80,60,70,60,75,85]
s=[0 for i in range(len(price)+1)]
calculatestack(price,s)
printstack(s,len(price))