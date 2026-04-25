class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        
        occurance=[]
        for i in range(len(nums)+1):
            occurance.append([])

        for key, value in hashmap.items():
            occurance[value].append(key)

        #loop backward
        res=[]
        track=0

        #loop through the whole occurance
        for i in range(len(nums),-1,-1):
            for num in occurance[i]:
                if track<k:
                    res.append(num)
                    track+=1
                else:
                    return res
        
        return res

            



"""
ideas: using bucket sort
    the idx gonna be the number of occurance
    each index gonna store a list of elem that have that number of occurance


create a hashmap such that:
    key: the elem
    val: the num of occurance

create a empty array with the elem be empty array

loop through that array, assign the number in nums to the correspond nth array

loop backward and add to a returned list

ex:  [1,2,2,3,3,3,4,4,4]
0   1        2       3   4   5   6   
    [1]     [2]     [3,4]


"""