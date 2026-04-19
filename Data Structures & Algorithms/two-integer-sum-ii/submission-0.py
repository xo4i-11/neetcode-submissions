class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #array of int : numbers (non decresing order)

        #return [idx1,idx2] indices start from 1 -> len(numbers) 
        # numbers[idx1] + numbers[idx2]=target
        #idx1<idx2 
        #only 1 valid solution

        for i in range (len(numbers)):
            for j in range (i+1,len(numbers)):
                if(numbers[i]+numbers[j]==target):
                    return [i+1,j+1]