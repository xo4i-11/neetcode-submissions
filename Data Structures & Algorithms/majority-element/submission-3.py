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
        
        
        
    
    """
    array: nums
    size of array: n

    majority elem is the elem appear > n/2 time in array
    majority elem will always exist in the array

    return majority elem

    def majority_elem(nums):
        hashmap={}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        
        for val in hashmap:
            if hashmap[val]>(len(nums)/2):
                return val

    """

    
        
        