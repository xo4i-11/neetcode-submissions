class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return

        l=0

        for r in range(len(nums)-k,len(nums)):
            temp=nums[r]
            nums[r]=nums[l]
            nums[l]=temp
            l+=1
        
        return

        

    """
    IDEAS:
    handle the case k=0 => return 
    Using 2 pointer. The simple idea is to swap the element that the pointer point to 
    for example: [1,2,3,4,5,6,7,8] => l=0, 

    for r in range(len(nums)-k,len(nums)):
        temp=s[r]
        s[r]=s[l]
        s[l]=temp
    
    return 
          
    

    """ 