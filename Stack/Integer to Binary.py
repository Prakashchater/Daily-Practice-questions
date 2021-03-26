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

    def bin_2_int(self,dec_num):
        s=Stack()
        while dec_num >0:
            r=dec_num%2
            s.push(r)
            dec_num=dec_num//2
        binary=""
        while not self.is_empty():
            binary+=str(s.pop())
        return binary


