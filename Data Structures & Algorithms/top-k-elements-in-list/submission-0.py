class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #num: [1,2,3,4]
        #k: 1
        #output in any order
        # answer is always unique 

        #CASE 1:
        # num: [1,2,3,4], k=1
        # output: [1] or [2] or [3] or [4]
        
        #CASE 2:
        #num: [1,2,2,3,3], k=1
        #output: [2] or [3]

        #CASE 3:
        #num: [1,2,2,3,3,3], k=2
        #output: [3,2] or [2,3]4

        hashmap={}
        array=[]
        returned=[]

        for i in range (len(nums)):
            if (nums[i] in hashmap):
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        
        #check the value from each key and get the k highest value
        comparator=99999
        for key in hashmap:
            if (hashmap[key]<comparator):
                array.append(hashmap[key])
                comparator=hashmap[key]
            else:
                array.insert(0,hashmap[key])

        
        for i in range (0,k):
            for key_1 in hashmap:
                if(hashmap[key_1]==array[i]):
                    returned.append(key_1)
        return returned


        