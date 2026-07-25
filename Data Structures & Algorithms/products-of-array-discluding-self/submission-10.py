class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = 1


        #count zero and find total without zero
        for num in nums:
            if num == 0:
                zero_count +=1
            else:
                total *= num
        
        if zero_count >=2:
            return [0]*len(nums)
        
        res = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)

            elif zero_count == 0:
                sum_except_that_num = int(total/num)
                res.append(sum_except_that_num)
        
        return res

        








"""
idea: 
    3 cases: + 1 zero
             + 0 zero
             + >+2 zero
    => count zero firt

"""
        