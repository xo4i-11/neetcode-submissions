class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        
        l = 0 
        r = len(nums)-1
        min_val = nums[0]

        while l <= r:
            m = (l+r)//2
            min_val = min(nums[m], min_val)

            if nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m - 1
            
        
        return min_val


        






"""
Question: 
    - the array (nums) have been rotated  
    - output: find the min num 

    [4,5,6,1,2,3]

    idea:
        - do binary search in the list
        - if the middle > right => we must move left ptr 
        - if the middle < left => we must move right ptr 
        - do it until found 

        [5,6,1,2,3,4]

        [3,4,5,6,1,2]

"""
        