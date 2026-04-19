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
    

                    
        