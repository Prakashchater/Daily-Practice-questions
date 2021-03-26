def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = "malayalam"
    print(palindrome(s))