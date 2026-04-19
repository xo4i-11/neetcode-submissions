class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #array of int : numbers (non decresing order)

        #return [idx1,idx2] indices start from 1 -> len(numbers) 
        # numbers[idx1] + numbers[idx2]=target
        #idx1<idx2 
        #only 1 valid solution

        #IDEAS:
        #create an hashmap, the the elem in list gonna be the key and the value gonna be the id
        hashmap=defaultdict(int)
        for j in range (len(numbers)):
            hashmap[numbers[j]]=j+1

        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff in hashmap and diff != i+1:
                return [min(i+1,hashmap[diff]),max(i+1,hashmap[diff])]
        
            