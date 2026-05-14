class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        
        count=0
        multiplication= 1

        for num in nums:
            if num == 0:
                count+=1
            else:
                multiplication*=num
        

        if count >=2:
            return [0]*len(nums)
        
        res=[]

        #case when there is 0 or 1
        for num in nums:
            if count==0:
                added_num=int( multiplication/num)
                res.append(added_num)
            elif count==1:
                if num==0:
                    res.append(multiplication)
                else:
                    res.append(0)
        
        return res
        
        













"""
idea: 3 case
    1 0
    2 0
    3 0

    => count the 0 and find the multiplication



"""