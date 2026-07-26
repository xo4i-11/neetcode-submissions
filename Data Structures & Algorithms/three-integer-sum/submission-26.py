class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # if the first num is already exceed the num
            if nums[i] > 0:
                break 
            
            # duplicate num
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if l<r and total>0:
                    r-=1

                elif l<r and total<0:
                    l+=1
                
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    #-1,-1,0,1,1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1

        return res                

            






"""
idea:
    - loop through every elem:
        + use 2 ptr for the elem on the right 

    -4, -1, -1, 0, 1, 2



"""
        