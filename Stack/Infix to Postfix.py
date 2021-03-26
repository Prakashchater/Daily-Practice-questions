class stack:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=[]
        self.array=[]
        self.output=[]
        self.precedence= {'+':1, '-':1, '*':2, '/':2, '^':3}

    def isempty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def push(self,op):
        self.top+=1
        self.array.append(op)

    def pop(self):
        if not self.isempty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"


    def isOperand(self,ch):
        return ch.isalpha()

    def notGreater(self,i):
        try:
            a=self.precedence[i]
            b=self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False

    def infixTopostfix(self,exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i== ')':
                while ((not self.isempty())and self.peek()!= '('):
                    a=self.pop()
                    self.output.append(a)
                if(not self.isempty() and self.peek()!= '('):
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isempty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isempty():
            self.output.append(self.pop())
        print("".join(self.output))

exp= "a+b*f"
obj= stack(len(exp))
obj.infixTopostfix(exp)