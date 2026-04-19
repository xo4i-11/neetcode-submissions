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



"""
IDEAS:
first, we will create the stack object with 2 fields: 
1: a stack so that we can store the element as usal, following the rule of LIFO
2: a min_stack so that we can track the smallest element by putting it at the end of the stack => get within O(1) using min_stack[-1]
"""

class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    def push(self,val:int):
        self.stack.append(val)
        
        if len(self.min_stack)==0:
            self.min_stack.append(val)
        else:
            min_val=min(self.min_stack[-1],val)
            self.min_stack.append(min_val)

    def pop(self):
        if len(self.stack)==0 or len(self.min_stack)==0:
            return 
        
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        if len(self.stack)==0:
            return 
        
        return self.stack[-1]

    def getMin(self):
        if len(self.min_stack)==0:
            return
        
        return self.min_stack[-1]

    







































