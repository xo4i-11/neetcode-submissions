class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l= 0
        r= len(nums)-1

        while l<=r:
            mid = (l+r)//2

            #if we found the target
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                l = mid + 1

            if target < nums[mid]:
                r= mid -1 
        
        return l 

            

"""
idea: 
    do the normal binary search
    if the target is not found in the lst:
        ex: target =1 , lst=[2]
        ex: target =3 , lst[2]
        => return l always correct
"""