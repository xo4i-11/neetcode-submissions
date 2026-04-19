class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        l=0
        r=len(nums)-1

        while l<= r:
            if nums[l]< nums[r]: #if the remaining sub-array is sorted
                res=min(res,nums[l])
                break

            m=(l+r)//2
            res=min(res,nums[m])

            #if left part is sorted
            if(nums[m]>=nums[l]):
                l=m+1
            else:
                r=m-1
        return res        

        #IDEAS:
        # we have a list [3,4,5,1,2]
        # For this question, i gonna use 2 pointer 
        # l = 0 and r = last idx => find the middle
        
        # if the middle value is in the left sorted part => we gonna move left ptr to the right sorted part
        #ex: [3,4,5] is left sorted part and [1,2] is right sorted part => we are at 5 -> move left ptr to 1
         
        #=> if m in left part, search the right
        # => if m in right part, search the left

    



    """
    ideas:
    we see that in the rotated sorted array, if we cut it into 2 part (cut in middle), we will always see that it always exist a sorted part 
    => we will use binary search to see which side is sorted
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
                break

            m=(l+r)//2
            res=min(res,nums[m])
            
            #[1,2,3,4,5] [3,4,5,6,1,2]
            #[3,4,5,1,2]; [5,1,2,3,4]; [1,2,3,4,5] [2,3,4,5,1] [3,4,5,1,2]
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return res
                





