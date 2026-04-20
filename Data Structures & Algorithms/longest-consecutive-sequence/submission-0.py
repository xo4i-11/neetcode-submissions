class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        for i in range(1,len(nums)):
            if(nums[i-1]+1==nums[i]):
                count+=1
        return count