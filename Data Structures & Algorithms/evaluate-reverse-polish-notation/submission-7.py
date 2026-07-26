class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        
        stack = []
        total = 0

        for c in tokens:
            if c == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif c == "-":
                res = - stack.pop() + stack.pop()
                stack.append(res)
            elif c  == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(b/a)
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        
        return stack[0]

                

"""
idea:
    use a stack
    ex: [1, 2, +, 3, *, 4]
        - we loop through every char:
            loop 1: stack = [1]
            loop 2: stack = [1,2]
            loop 3: when we meet +, we turn it into 1+ 2 => stack = [3]

        


"""
        