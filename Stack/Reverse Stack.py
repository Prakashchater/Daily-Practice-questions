class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

def reverse_stack(stack,input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str=""
    while not stack.is_empty():
        rev_str+=stack.pop()
    return rev_str

if __name__ == '__main__':

    stack=Stack()
    input_str="Hello"
    print(reverse_stack(stack,input_str))

