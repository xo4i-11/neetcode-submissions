class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset= []

        def backtrack():
            # base case: only add to res when we had all the elem in subset
            if len(subset) == len(nums):
                res.append(subset.copy())
                return 
            
            #try every number as the next choice
            for num in nums:
                # Skip numbers that are already used
                # in the current permutation
                if num not in subset:
                    #choose
                    subset.append(num)
                    #explore
                    backtrack()   
                    #undo choice (back track)
                    subset.pop()   
        
        backtrack()
        return res