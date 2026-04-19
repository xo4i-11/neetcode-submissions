class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array=[]
        for i in range(len(nums)):
            index_num=1
            for j in range(len(nums)):
                if(i!=j):
                    index_num=nums[j]* index_num
            array.append(index_num)
        return array