class Solution:
    def reorganizeString(self, s: str) -> str:
        #create hashmap to store the occurance of each char
        hashmap = {}
        for c in s:
            if c not in hashmap:
                hashmap[c]=1
            else:
                hashmap[c]+=1
            
        maxHeap=[]

        #we sort by the count
        for char, count in hashmap.items():
            maxHeap.append([-count, char])

        heapq.heapify(maxHeap) #O(n)

        #track prev char in order not to reuse it
        prev = None
        res= ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            #most frequent, except prev
            count, char = heapq.heappop(maxHeap)
            res += char
            count+=1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count != 0:
                prev = [count, char]

        return res






"""
idea:





"""
        