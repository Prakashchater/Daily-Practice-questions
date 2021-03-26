#O(N^2) time and O(N)
# def palindromecheck(string):
#     rev_str=""
#     for i in reversed(range(len(string))):
#         rev_str+=string[i]
#     return string==rev_str
# #O(N) time and O(n) space
# def ispalindrome(string):
#     rev_str=[]
#     for i in reversed(range(len(string))):
#         rev_str.append(string[i])
#     return string==''.join(rev_str)

# O(N) time and O(1) space
def ispalindrome(string):
    leftidx=0
    rightidx=len(string)-1
    while leftidx<rightidx:
        if string[leftidx]!=string[rightidx]:
            return False
        leftidx+=1
        rightidx-=1
    return True

string='abcdcbaf'
print(ispalindrome(string))