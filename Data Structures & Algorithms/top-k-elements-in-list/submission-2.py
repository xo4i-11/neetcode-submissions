class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#IDEAS:
#Using the bucket sort 
#the index gonna be the number of occurance of the elment in the list (0->len(n))
#the list that store elems that have the occurance correspond to the index
#for example: [1,2,2,3,3,3,4,4]
# 0 1->[1] 2->[2,4] 3-> [3] 
#=> we gonna traverse from right to left to get the k most frequent


#to find the occurance of each elem, i gonna use the hashmap with key= elem and value = there occurance
        hashmap={}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1


        #we gonna create the bucket with the number of bucket = len(nums)
        bucket_list=[[] for i in range (len(nums)+1)]
        #the bucket gonna store the number of occurance

        for key, value in hashmap.items():
            bucket_list[value].append(key)

        #afterwards, adding it to the bucket, it will have the following form 
        # [1,2,2,3,3,3,4,4]
        # 0 1->[1] 2->[2,4] 3-> [3]  => [0,1 [1],2 [2,4],3 [3],4,5,6,7,8]

        res=[]

        for j in range(len(nums),0,-1): 
            for ele in bucket_list[j]:
                res.append(ele)
                if(len(res)==k):
                    return res

        return res































