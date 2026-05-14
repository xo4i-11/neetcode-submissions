class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first, filter out dup num
        numSet= set(nums)
        streak=0

        for num in nums:
            if num-1 in numSet:
                continue
            
            length=0
            while num+length in numSet:
                length+=1
            
            streak=max(streak,length)

        return streak
            


        

        