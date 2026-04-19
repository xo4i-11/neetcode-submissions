class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={} 
        
        idx=0
        #create a hashmap and assign the key with value in list and value with the idx
        for num in nums:
            dict[num]=idx
            idx+=1
        
        # check if the other number in the sum is available or not
        for i in range(len(nums)):
            diff=target - nums[i]
            if(diff in dict and dict[diff]!=i):
                return [i,dict[diff]]
        





        