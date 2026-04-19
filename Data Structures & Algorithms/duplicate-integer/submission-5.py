class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_of_num=set() #use set because if use [], the run time of num in set_of_num =O(n^2)
        for num in nums:
            if num in set_of_num:
                return True
            else:
                set_of_num.add(num)
        return False



#IDEAS:
#we want to check duplicate 
# => the fastest ds that help us check the unique is gonna be set



"""
//STUPID APPROACH SINCE THE ARRAY WAS NOT SORTED
def check_dup(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            return True
    return False

    

// BETTER APPROACH
def check_dup(nums);
    seen=set()
    for n in nums:
        if n in seem:
            return True
        else:
            seen.add(n)
    return False
"""









#


































