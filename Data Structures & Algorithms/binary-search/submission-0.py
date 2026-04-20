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
        #if the middle > target => move left
        #else: move right 
        
        middle= math.floor(len(nums)/2)

        if(target<= middle):
            for i in range (0,middle):
                if target == nums[i]:
                    return i
        else:
            for j in range (middle, len(nums)):
                if target==nums[j]:
                    return j
        return -1
        
        