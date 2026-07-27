class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. find the min val 
        l = 0
        r = len(nums) -1
        min_val = nums[0]
        min_idx = 0
        n = len(nums) - 1

        while l<=r:
            m = (l+r)//2
            min_val = min(min_val, nums[m])
            
            if min_val == nums[m]:
                min_idx = m


            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
        
        if min_idx == 0:
            return self.binary_search(0, n, target,nums)

        elif nums[0] <= target <= nums[min_idx-1]:
            return self.binary_search(0,min_idx-1, target,nums)
        
        elif nums[min_idx] <= target <= nums[n]:
            return self.binary_search(min_idx,n,target,nums)
        
        return -1
        



    def binary_search(self,l,r,target, nums):
        while l<=r:
            m = (l+r)//2

            if nums[m] > target:
                r = m - 1 
            
            elif nums[m] < target:
                l = m + 1
            
            else:
                return m
            
        return -1




            
        


    





"""
problem:
    - given a rotated array and a target
    - return idx within nums. If not present => return -1

idea:
    1. find the min value in the array first, find its index  (min_index) 
        ex: [4,5,6,7,0,1,2]
            + min_val = 0, min_index = 4

        since we found the idx of min_val (0), we can separate the 2 sorted part
    
    2. there will be 3 cases happen:
        - if the target is in the left sorted (ex: target = 5)  
            + it happens when: nums[0] < target < nums[min_index-1]
                => l = 0, r = min_index-1

        - if the target is in the right sorted (ex: target = 1)
            + it happens when: nums[min_index] < target < nums[len(arr)]

            => l = min_index, r = len(arr) - 1

        - edgde case: 
            + in a list of [0,1,2,3,4,5,6,7]
                + it happens when: min_index = 0
                    => it is already in correct order, we just gonna do normal binary search:
                    => l = 0, r = len(arr) - 1
        

"""
        