class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #storing them in an hashmap, key is the value in the list and value is the idx
        hashmap={}
        
        for i in range (len(nums)):
            hashmap[nums[i]]=i
        
        # we can loop through the whole list
        #for each elem in the list, we gonna find if diff=target-elem is in the hashmap or not
        #if yes,return the [min(i,nums[i]),max(i,nums[i])]

        for j in range (len(nums)):
            diff=target- nums[j]
            
            if(diff in hashmap and hashmap[diff]!=j):
                return [min(j, hashmap[diff]), max(j, hashmap[diff])]
        
        return []

            

"""
            
# IDEAS:
# using an hashmap to store the elem with its respective index
#loop through every elem and check if diff = target-elem is in the arr or not,
#if yes, return the idx
#if no, keep looping



hashmap={}
for i in range(len(nums)):
    hashmap[nums[i]]=i

for j in range(len(nums)):
    diff= target - nums[j]

    if diff in hashmap and hashmap[diff]!=j:
        return [min(hashmap[diff],j), max(hashmap[diff],j)]
    
return []

"""


"""
def two_sum(nums,target):
    hashmap={}

    for i in range(len(nums)):
        hashmap[nums[i]]=i
    
    for j in range(len(nums)):
        diff=target-nums[j]

        if diff in hashmap and hashmap[diff]!=j:
            return [j,hashmap[diff]]
    
    return []
    
"""

    



    

            

        