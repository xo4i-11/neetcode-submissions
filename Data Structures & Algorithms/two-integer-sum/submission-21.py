class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return []
        
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        
        res=[]
        

        for j in range(len(nums)):
            diff = target - nums[j]
    
            if diff in hashmap and hashmap[diff]!=j:
                res.append(j)
                res.append(hashmap[diff])
                return res
        
        return res
            
        