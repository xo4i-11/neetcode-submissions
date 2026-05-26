class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True

        hashmap={"}": "{", ")" : "(", "]" : "["}
        stack=[]

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
                    
        if len(stack)==0:
            return True
        else:
            return False

        
        