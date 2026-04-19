class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r= len(nums)-1

        while l<=r:
            m= (l+r)//2

            if target== nums[m]:
                return m
            
            #left sorted part
            if(nums[m]>=nums[l]):
                if target > nums[m]:
                    l=m+1
                elif target < nums[l]:
                    l=m+1
                else: # target between the left sorted part 
                    r=m-1

            #right sorted part 
            else:
                if target < nums[m]:
                    r=m-1
                elif target > nums[r]:
                    r= m-1
                else:
                    l=m+1
            
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

