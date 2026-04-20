class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_array=[]
        for i in range (len(nums)):
            j=i+1
            for j in range (len(nums)):
                if (nums[i]+nums[j]==target):
                    idx_array.append(i);
                    idx_array.append(j);
                    return idx_array
        return idx_array


        