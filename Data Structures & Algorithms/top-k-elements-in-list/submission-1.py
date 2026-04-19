class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we gonna use the bucket sort

        #we gonna make a hasmap: 
        # +) key is the idx adn it represent the occurance time . ex: [1,1,1,2,2,3]=> key: 0->6
        # +) value are the set of element that occur the same number of times

        #) loop from the end to find the the list of value that have the most number of occurance

        #[1,2,2,3,3,3] k=2 => output:[2,3]

        #first: i gonna create a hasmap to track the number of occurance of each value
        count={}
        for num in nums:
            if(num in count):
                count[num]+=1
            else:
                count[num]=1
        
        #second: using the bucket sort.
        # i am gonna create an array that store list of value that have the occurance the same as the index
        #for examle:[1,2,2,3,3,3,4]
        
        #consider the idx as the key and it represent the number of occurance
        #the value gonna be the list of value that occur idx times

        #create a list of  len(nums)+1 list inside
        occur=[[] for i in range (len(nums)+1)]
        
        for key, value in count.items():
            occur[value].append(key)
        #[[],[1,4],[2],[3],[],[],[]]

        #from now, we gonna loop backward the oocur to get the highest number of occurance element
        res=[]

        for j in range (len(occur)-1,0,-1):
            for element in occur[j]:
                res.append(element)
                if(len(res)==k):
                    return res

    #run time: O(n)


        