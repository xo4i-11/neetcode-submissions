class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]]=i
        
        for j in range(len(nums)):
            diff = target - nums[j]

            if diff in hashmap and hashmap[diff] != j:
                return [min(hashmap[diff], j), max(hashmap[diff], j)]
        
        
        


        