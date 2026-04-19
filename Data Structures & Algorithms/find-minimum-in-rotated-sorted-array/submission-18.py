class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        ideas:
        we gonna do the binary search(dont care about the order of the element)
        what we trynna do is to set the right and the left pointer poiting to the min element 
        => we will find mid = (l+r)//2

        [3,4,5,6,1,2]

        if mid point >= the right pointer => it means that the min elem must be somewhere between mid point and right pointer
        => we move left pointer

        elif mid point < right pointer: => the mid point could be the min => we will seet right ptr to mid and keep doing binary search
            => r=mid
        
        return nums[l]

        [6,1,2,3,4,5]
        
        """
        
        l=0
        r=len(nums)-1
        
        while l<r:
            mid=(l+r)//2
            
            if nums[mid]> nums[r]:
                l=mid+1
            else:
                r=mid
        
        return nums[l]


    



    """
    ideas:
    we see that in the rotated sorted array, if we cut it into 2 part (cut in middle), we will always see that it always exist a sorted part 
    => we will use binary search to see which side is the mid point in by comparing the mid point with the left most value
    
    we will determine which side is the mid point in by 
    if left half is sorted => the the min value must be in the right half
    if right half is sorted => the min must be in the left half or at the mid point

    """
    def rotated_array(nums):
        l=0
        r=len(nums)-1
        res=nums[0] # since nums[0] might be the smallest value

        while l<=r:
            if nums[r]>nums[l]:
                res=min(res,nums[l])
                return res

            m=(l+r)//2
            res=min(res,nums[m])
            
            #[1,2,3,4,5] [3,4,5,6,1,2]
            #[3,4,5,1,2]; [5,1,2,3,4]; [1,2,3,4,5] [2,3,4,5,1] [3,4,5,1,2]
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return res

#SAME IDEA
    #IDEAS:
    # we have a list [3,4,5,6,1,2]
    # For this question, i gonna use 2 pointer 
    # l = 0 and r = last idx => find the middle
    
    # if the middle value is in the left sorted part => we gonna move left ptr to the right sorted part
    #ex: [3,4,5] is left sorted part and [1,2] is right sorted part => we are at 5 -> move left ptr to 1
        
    #=> if m in left part, search the right
    # => if m in right part, search the left








        

"""

do normal binary search
l=0
r=len(nums)-1

while l<r:
    mid = (l+r)//2
    if mid > r:
        l= r+1
    else:
        r=mid 
    

return nums[l]
    







"""








































                





