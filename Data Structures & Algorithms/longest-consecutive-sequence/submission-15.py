class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # only start with the first letter of the sequences
            if num-1 not in numSet:
                length = 0 

                #start from the first elem, then count the whole sequences
                while num + length in numSet:
                    length +=1
                
                longest = max(length, longest)
        
        return longest
                    

        




 ##IDEAS:
        # check the left neighbor of every value in the list to figure out if it is a start of a sequence or not
        #for ex:
        # [100,4,200,1,3,2]
        # 100->
        # 200->
        # 1->2->3->4->
            
            



        