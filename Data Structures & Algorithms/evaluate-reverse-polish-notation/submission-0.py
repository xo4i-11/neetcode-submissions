class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

#given an array of strings, represent a valid arithmetic expression 
# return the result in INTEGER
# rounded to the the lowest int  (floor)


#ex:
# 2, 1 ,+, 3, *

#we gonna create a stack and every time we loop though the char,we gonna add it to the stack 
#we gonna loop until seeing the operator => we gonna pop the number and store the result of that operation in the stack

#ex: 2, 1 ,+, 3, *
# after looping for a while, the stack have: stack=[2,1]
# when reaching "+" => stack first pop the elems and add the result of operation => stack=[3]
# next, when looping through 3 => stack will be: stack=[3,3]
# when reaching "*" => stack pops the elem and add the result of operation => stack=[9]

        stack =[]
        for c in tokens:
            if c == "+":
                res=stack.pop() + stack.pop()
                stack.append(res)
            elif c == "-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif c == "*":
                res= stack.pop() * stack.pop()
                stack.append(res)
            elif c == "/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))

            else: #the number
                stack.append(int(c))
        
        return stack[-1]

                



