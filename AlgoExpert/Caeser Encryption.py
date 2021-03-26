# O(n) time and O(n) space
def caeserCypherEncryption(string,key):
    new_letter=[]
    new_key=key % 26
    for letter in string:
        new_letter.append(getnewLettercode(letter,new_key))
    return "".join(new_letter)

def getnewLettercode(letter,key):
    newLettercode=ord(letter)+key
    return chr(newLettercode) if newLettercode <=122 else chr(96+newLettercode % 122)

if __name__ == '__main__':
    string="abcdefghijklmnopqrstuvwxyz"
    key=2
    print(caeserCypherEncryption(string,key))

