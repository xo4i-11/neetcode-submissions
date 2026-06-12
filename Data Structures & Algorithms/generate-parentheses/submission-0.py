class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = []

        def dfs(open_number, closed_number):
            #when we are at the leaf
            if open_number == closed_number == n:
                string = "".join(stack)
                res.append(string)
                return 
            
            #add the open parenthis if open < n
            if open_number < n:
                stack.append("(")
                dfs(open_number+1, closed_number)
                stack.pop()
            
            if closed_number < open_number:
                stack.append(")")
                dfs(open_number, closed_number+1)
                stack.pop()
            
        dfs(0,0)
        return res

            






"""
idea:
    use backtracking
    - we only add the open parenthesis if open < n
    - we only add the close parenthesis if close < open
    - valid IFF open == closed == n




"""