class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        l=0
        r=len(nums)-1

        while l<r:
            temp=nums[r]
            nums[r]=nums[l]
            nums[l]=temp
            l+=1
            r-=1
        
        l=0
        r=k-1

        while l<r:
            temp=nums[r]
            nums[r]=nums[l]
            nums[l]=temp
            l+=1
            r-=1
        
        l=k
        r=len(nums)-1
        while l<r:
            temp=nums[r]
            nums[r]=nums[l]
            nums[l]=temp
            l+=1
            r-=1
        
        return
    

        

    """
    IDEAS: using 2 pointer 

    we got an array: [1,2,3,4,5], k=2
    => we gonna reverse the array => [5,4,3,2,1]
    after that, we gonna split the reversed array into 2 part, [5,4] and [3,2,1] (split base on k)
    we gonna reverse [5,4]-> [4,5] and [3,2,1]->[1,2,3]
    => the returned array = [4,5,1,2,3]
    

    """ 