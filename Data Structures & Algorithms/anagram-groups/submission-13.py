class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] += 1
            
            hashmap[tuple(count)].append(s)
        
        return list(hashmap.values())

    






"""

[1a, 1c, 1t] : ]["cat", "act","tac"]

"""
        





"""
idea: loop through each word. store in hashmap such that: key= count_lst, val= array store the word that have same count 
if 2 word have the same count => put in a list and add to the main list


"""
def group_anagram(strs):
    hashmap= defaultdict(list)

    for w in strs:
        count = [0]*26

        for c in w:
            count[ord(c)-ord('a')] +=1
        
        hashmap[tuple(count)].append(w)

    return list(hashmap.values())




























