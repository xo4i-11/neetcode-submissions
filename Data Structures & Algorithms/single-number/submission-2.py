class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #non empty array => dont need to check len(array)
        res=0 # n xor 0=n
        for n in nums:
            res= n^res # ^ is xor
        return res

        
        #2  ...0010
        #4  ...0100 
        #4  ...0100 
        #1  ...0001
        #1  ...0001