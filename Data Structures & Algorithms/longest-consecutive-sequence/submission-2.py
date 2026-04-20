class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==1:
            return 1
            
        count=0
        for j in range(1,len(nums)):
            if(nums[j-1]+1==nums[j]):
                count+=1
                break

        
        for i in range(1,len(nums)):
            if(nums[i-1]+1==nums[i]):
                count+=1
        return count