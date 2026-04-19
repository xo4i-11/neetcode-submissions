class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #array of int : numbers (non decresing order)

        #return [idx1,idx2] indices start from 1 -> len(numbers) 
        # numbers[idx1] + numbers[idx2]=target
        #idx1<idx2 
        #only 1 valid solution

    

                    
        

        hashmap={}
    
        
        for i in range(len(numbers)):
            subtraction=target-numbers[i]
            if(subtraction in hashmap):
                return [min(i,hashmap[subtraction])+1,max(i,hashmap[subtraction])+1]
            hashmap[numbers[i]]=i
        return []