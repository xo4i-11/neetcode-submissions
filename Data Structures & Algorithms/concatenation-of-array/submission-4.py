class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        
"""
IDEAS:

 create a new array: ans
loop through every num in nums=> for n in nums
since we need to double it
 => for i in range(2):
        for n in nums:

IMPLEMENTATION:
    def getConcatenation
        ans=[]
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans 
"""