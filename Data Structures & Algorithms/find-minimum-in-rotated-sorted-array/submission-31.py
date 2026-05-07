class Solution:
    def findMin(self, nums: List[int]) -> int:
        res= float("inf")
        for num in nums:
            if num < res:
                res= num
        return res

        