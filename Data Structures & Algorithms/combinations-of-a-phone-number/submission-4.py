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




"""
idea: 


"""

def letter_comb(digits):
    res = []
    curr_word = ""

    hashmap = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }

    def dfs(i):
        nonlocal curr_word
        if len(curr_word) == len(digits):
            res.append(curr_word)
            return 
        
        char = digits[i]
        for c in hashmap[char]:
            curr_word += c
            dfs(i+1)

            curr_word = curr_word[0:len(curr_word)-1]
        
    if digits:
        dfs(0)
    
    return res






























