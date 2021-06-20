class Stack:
    def __init__(self):
        self.myStack = []
        
    def push(self, item):
        self.myStack.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.myStack.pop()
        return "Stack is Empty"
    
    def isEmpty(self):
        return len(self.myStack) == 0
    
    def top(self):
        if not self.isEmpty():
            return self.myStack[len(self.myStack) - 1]
        return "Stack is Empty"
    
    def printStack(self):
        if not self.isEmpty():
            i = len(self.myStack) - 1
            while i >= 0:
                print(self.myStack[i])
                i-=1
            return
        return "Stack is Empty"

        