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



"""


#IDEAS:
#idx in the array gonna act as the occurance and the value gonna be place at that idx
# 0   1   2     3          4      5 
# [] [1]  [2]  [3,4]    []     []

hashmap={}

for num in nums:
    if num in hashmap:
        hashmap[num]+=1
    else:
        hashmap[num]=1

occur =[[] for i in range(len(nums)+1)]

for key, values in hashmap.items():
    occur[value].append(key)

res=[]

for i in range(len(nums),0,-1):
    for char in occur[i]:
        res.append(char)
        if(len(res)==k):
            return res
return res










#IDEAS: Using bucket sort
#store the elem with their occurance inside a hashmap
#we we gonna store them in list such that the index is the number of occurance(occurance run from 0-> len(num))
#the list gonna be the elem with correspond number of occurance

hashmap={}

for num in nums:
    if num in hashmap:
        hashmap[num]+=1
    else:
        hashmap[num]=1
    

big_bucket=[]

for i in range (len(nums)+1):
    big_bucket.append([])

for key, value in hashmap.items():
    big_bucket[value].append(key)

    #[1],[2],[3,4] k=2

res=[]

for j in range(len(nums),-1,-1):
    for elem in big_bucket[j]:
        res.append(elem)
        if len(res)>=k:
            return res
return res
        

"""










































