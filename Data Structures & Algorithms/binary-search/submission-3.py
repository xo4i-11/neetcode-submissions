class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #array of integer: nums 
        #+) those num must be unique
        #=) sorted from small -> large

        #int target

        #check if target in nums:
        #+) if it is correct => return the idx
        #+) else: return -1

        #run in O(log(n))


        #IDEAS:
        # to run in O(log(n) => we need to use the binary search => we search only half of it
        # we gonna split it into 2 part (find middle)
        #compare to the target, 
        #if the middle > target => split left side in half, set the mid and keep do it 
        #else: split the right side in halp and keep do it
        
    
        left=0
        right=len(nums)-1

        while left<=right: #REMEMBER <=, NOT <
            mid= (left+right)//2
            if(nums[mid]>target):
                right=mid-1
            elif nums[mid]< target:
                left=mid +1
            else:
                return mid
        return -1
        



        
"""
using binary search

we gonna use a pointer at the start and another ptr at the end
after that, we gonna find the middle position of nums
if the elem at the middle positon is > target => set the right ptr to the positon mid-1
if the elem at the middle position is < target => set the left ptr to the position mid+1
else: return the idx
if not found => return -1
"""

def binary_search(nums,target):
    l=0
    r=len(nums)-1

    while l<=r:
        mid = (r+l)//2

        if nums[mid] == target:
            return mid 

        elif nums[mid]>target:
            r=mid-1
        elif nums[mid]<target:
            l=mid+1
     
    return -1



























