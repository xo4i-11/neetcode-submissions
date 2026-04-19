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
                

            


            
# IDEAS:
# add all the number in nums into the hashmap that have key=number and value=index
# 




            

        