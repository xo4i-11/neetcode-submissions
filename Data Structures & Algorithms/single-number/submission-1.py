class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #non empty array => dont need to check len(array)
        seen=set()
        for num in nums:
            if(num in seen):
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]

        
        