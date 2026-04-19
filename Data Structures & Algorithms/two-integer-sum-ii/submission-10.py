class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        #array of int : numbers (non decresing order)

        #return [idx1,idx2] indices start from 1 -> len(numbers) 
        # numbers[idx1] + numbers[idx2]=target
        #idx1<idx2 
        #only 1 valid solution
        l,r=0, len(numbers)-1
        
        while(l<r):
            curSum=numbers[l]+numbers[r]
            
            if curSum>target:
                r-=1
            elif curSum<target:
                l+=1
            else:
                return [l+1,r+1]
        return []
    



"""
        l=0
        r=len(nums)-1

        while l<r:
            total=nums[l]+nums[r]
            if l<r and total>target:
                r-=1
            elif l<r and total<target:
                l+=1
            else:
                return [l+1,r+1]
        return []

                    
        


IDEAS:
1 ptr gonna start at the head and another start at the tail
while l<r:
    find the sum of those 2 elem at the idx that the ptr points at
    if the sum>target => move right ptr to the left'
    if sum<target => move left ptr to right

    if equals:
        return the idx




#given an array of int that is NON-DECREASING

def two_sum(numbers,target):
    l=0
    r=len(numbers)-1

    while l<r:
        total= numbers[l]+numbers[r]

        if l<r and total<target:
            l+=1
        if l<r and total>target:
            r+=1
        else:
            return[l+1,r+1]
    
    return []
"""






















































