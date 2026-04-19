class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1

        for key,val in hashmap.items():
            if val > len(nums)//2:
                return key
        
        
        
        
        
        