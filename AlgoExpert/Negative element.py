# O(N) time and O(1) Space

def negative(number,n):
    j=0
    for i in range(0,n):
        if number[i] < 0:
            number[i], number[j]= number[j], number[i]
            j+=1
    return number

if __name__ == '__main__':
    number= [-8,2,-1,6,-3,7,3]
    n=len(number)
    print(negative(number,n))


