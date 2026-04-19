class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            mid= (l+r)//2

            if nums[mid]==target:
                return mid
            
            if nums[mid]>= nums[l]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            
            else:
                if nums[r]>=target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            
        return -1

                
                 

#IDEAS:
# [4, 5, 6, 7, 0, 1, 2]
# l=4, r=2, m=7, consider target=0

#first, check which sorted part is the middle in
# if in left sorted part, known that 0< 7 => we check if the target is smaller than the first char (4) or last char or no
#=> if yes -> search the right sorted part
# => if no => search the left sorted part

#=> since 0 is < 4 => it search the [0,1,2] part
#l=0 and r=2 => m=1
#since 1 is right sorted part => if target (0) <1 => move the right pointer to 0
#if target > 1 => move left ptr to 2









'''
IDEAS:
we will find the mid point first and check which sorted part is it in.

First, we will check if the mid point is the target or not. If yes => return 

next, if the midpoint in left part => move the right pointer to the midpoint 
if the midpoint in right part => move the left ptr to midpoint 




'''












"""
we do binary search, search for mid 
we will figure out which part it is in 
if it in left sorted => binary search in that part
if it in right sorted => binary search in that part

"""


#   4   5    6   7    0   1    2   3 
#   

def search_in_rotated_array(nums,target):
    l=0
    r=len(nums)-1

    while l<r:
        mid= (l+r)//2

        if nums[mid]==target:
            return mid

        if nums[mid]>nums[l]:
            if target > nums[mid]:
                l=mid +1
            if target < nums[l]:
                l=mid+1
            else:
                r=mid-1
        
        else:
            if target < nums[mid]:
                r= mid-1
            elif target > nums[r]:
                r=mid-1
            else:
                l=mid+1

    return -1







        







"""   
find the mid point like doing the normal binary search

we will compare the midpoint with the target:
if nums[mid]=target => return

if the mid is in the left sorted part:
    if the target > nums[mid]:
        l= mid +1
    elif target > nums[l]:
        r= mid-1
    else:
        l=mid+1

if mid in right sorted part:
    if target > nums[r]:
        r= mid-1
    elif target < nums[mid]:
        r=mid-1
    else:
        l=mid+1


re



# 3  4   5   6   7   0   1   2   3
# .                      .       . 

"""







    

    











































