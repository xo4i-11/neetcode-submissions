class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        
        if not self.minStack:
            self.minStack.append(val)
        else:
            min_val= min(val,self.minStack[-1])
            self.minStack.append(min_val)

        

    def pop(self) -> None:
        if not self.stack:
            return
        
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]   
        

    def getMin(self) -> int:
        return self.minStack[-1]
        



#IDEAS:
# Create 1 stack to implement the function while other will track the min element everytime a value
# is added or removed in the main stack => the smallest element will always be on the top => O(1)
