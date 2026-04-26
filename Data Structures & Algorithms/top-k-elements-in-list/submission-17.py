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
# [] [1]  [2]  [3,4]       []    []

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
        



#bucket sort
#loop through all num in nums and track their occurance
#store them inside a list such that the idx is their occurance, the num will be stored inside an array
#loop from the back 


hashmap={}

for num in nums:
    if num in hashmap:
        hashmap[num]+=1
    else:
        hashmap[num]=1


count_list=[]
for i in range(len(nums)+1): #=> run from 0-> len(nums)
    count_list.append([]) # create bucket

#we gonna put the elem with the same occurance num in a list => key=idx=occurance; value=list of correspond elem
for key, value in hashmap.items():
    count_list[value].append(key)

res=[]
#[1],[2][3,4]
for j in range(len(nums),-1,-1):
    for elem in hashmap[j]:
        res.append(elem)
        if len(res)>=k:
            return res

return res
"""



"""

#bucket sort
# the idx gonna be the num of occurance of the elem 

hashmap={}

for num in nums:
    if num in hashmap:
        hashmap[num]+=1
    else:
        hashmap[num]=1


#create len(nums) empty placeholder which represent the occurance of the elem
bucket_list=[]

for i in range(len(nums)+1):
    bucket_list.append([])

for key, value in hashmap.items():
    bucket_list[value].append(key)

res=[]
#[1],[2][3,4]
for j in range(len(nums),-1,-1):
    for elem in bucket_list[j]:
        res.append(elem)
        if len(res)>=k:
            return res

return res
"""
    












#bucket sort
"""
we wanna store the element in the right bucket
the idx of the bucket represent the number of occurance of that element 
[1,2,2,3,3,3]

we got a bucket_list with the max idx = the max possible occurance. in this case: 6

=> first, we wanna create an bucket_list with 6 empty list so that we can append the number in
we will assign the elem above to the right bucket

afterwards, loop from backward, stop when reach k

"""


def top_k_frequent_elems(nums,k):

    #create a valid bucket list with the right number of buckets
    bucket_list=[]
    for i in range(len(nums)+1):
        bucket_list.append([])

    #find the occurance of the elem
    hashmap={}
    for num in nums:
        if num in hashmap:
            hashmap[num]+=1
        else:
            hashmap[num]=1

    #assign the elem to the right bucket
    for key, value in hashmap.items():
        bucket_list[value].append(key)

    res=[]

    for i in range(len(nums),-1,-1):
        bucket=bucket_list[i]

        for elem in bucket:
            res.append(elem)
            k-=1
            if k<=0:
                return res
            
    
    return res

    


     

    































































