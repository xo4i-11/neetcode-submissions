class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        count=0
        total=0

        for i in range(len(nums)):
            total+=nums[i]
            prefix_sum = total-k

            if prefix_sum in hashmap:
                count+=hashmap[prefix_sum]
            
            if total in hashmap:
                hashmap[total]+=1
            else:
                hashmap[total]=1
        
        return count