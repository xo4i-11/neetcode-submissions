class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_stack.append(val)
        
        else:
            self.stack.append(val)
            min_val = min(val, self.min_stack[-1])
            self.min_stack.append(min_val)

        return 
        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return 
        
        self.stack.pop()
        self.min_stack.pop()
        return 

    def top(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return -1
        return self.min_stack[-1]
        
