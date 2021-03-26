def operator(x):
    if x=='+':
        return True
    if x=='-':
        return True
    if x=='*':
        return True
    if x=='/':
        return True
    if x=='^':
        return True
    return False

def postTOpre(p):
    s=[]
    l=len(p)
    for i in range(l):
        if (operator(p[i])):
            op1=s[-1]
            s.pop()
            op2=s[-1]
            s.pop()
            temp= p[i]+op2+op1
            s.append(temp)
        else:
            s.append(p[i])

    ans=""
    for i in s:
        ans+=i
    return ans

if __name__ == '__main__':
    p="ab+c-def^^*g/"
    print("prefix: ", postTOpre(p))