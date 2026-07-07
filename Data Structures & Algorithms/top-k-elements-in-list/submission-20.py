class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        #create a bucket
        for i in range(len(nums)+1):
            buckets.append([])

        #track the number of occurance 
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num] = 1
        
        for key, val in hashmap.items():
            buckets[val].append(key)
        
        res=[]

        for i in range(len(nums), -1, -1):
            for elem in buckets[i]:
                res.append(elem)
                if len(res) == k:
                    return res
        
        return res

        