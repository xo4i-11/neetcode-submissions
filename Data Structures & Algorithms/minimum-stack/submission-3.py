class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        if len(self.stack)== 0:
            self.min_stack.append(val)
            self.stack.append(val)
            return

        self.stack.append(val)
        min_val= min(self.min_stack[-1], val)
        self.min_stack.append(min_val)
        return         

    def pop(self) -> None:
        if len(self.stack)==0:
            return 
        
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack)==0:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.min_stack)==0:
            return -1
        return self.min_stack[-1]
