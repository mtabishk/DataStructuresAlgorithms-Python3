class Stack:
    def __init__(self):
        self.myStack = []
        
    def push(self, item):
        self.myStack.append(item)
        
    def pop(self):
        return self.myStack.pop()
    
    def isEmpty(self):
        return len(self.myStack) == 0
    
    def top(self):
        return self.myStack[len(self.myStack) - 1]
    
    def printStack(self):
        self.revmyStack = self.myStack.reverse()
        for i in self.revmyStack:
            print(i)