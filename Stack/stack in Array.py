from sys import maxsize     #maxsize attribute of the sys module
                            # fetches the largest value a variable of
                            # data type Py_ssize_t can store.
def createsatck():
    stack=[]
    return stack

def isempty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print(item, "Push in Stack")

def pop(stack):
    if isempty(stack):
        return str(-maxsize-1)   #return minus infinite

    return stack.pop()

def peek(stack):
    if isempty(stack):
        return str(-maxsize-1)

    return stack[len(stack) - 1]

stack = createsatck()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
print(pop(stack) + " Popped from stack")
print(isempty(stack))
# print(pop(stack) + " Popped from stack")
# print(pop(stack) + " Popped from stack")


