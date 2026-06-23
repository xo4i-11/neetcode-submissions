class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        curr_str = ""
        
        def dfs(i):
            nonlocal curr_str 
            if i == len(digits):
                res.append(curr_str)
                return 
            
            for c in hashmap[digits[i]]:
                curr_str+=c
                dfs(i+1)

                #keep everything except the last char (backtrack)
                curr_str = curr_str[0:-1]
        
        if digits:
            dfs(0)
        
        return res