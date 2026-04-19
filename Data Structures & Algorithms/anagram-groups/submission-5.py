class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list) #mapping charCount to the list of diagram for ex: [1e 1a 1t]:["eat","ate","tea"]
        # for ex: hashmap["greet"].append("hello") -> {"greet":["hello"]} -> default value is []
        for string in strs:
            count=[0] * 26 #a...z (create a list with 26 element and initialize it with 0)

            for char in string:
                count[ord(char)-ord("a")]+=1

            hashmap[tuple(count)].append(string) #have to use tuple since key must be immutable 

        return list(hashmap.values())




"""
#IDEAS: [1a 1c 1t] : [act, cat]
hashmap=defaultdict(list) #init all the value to []

for s in strs:
    count =[0]*26
    for c in s:
        count[ord(c)-ord("a")]+=1
    #[1a 1c 1t]
    hashmap[tuple(count)].append(s)

return list(hashmap.values())






#IDEAS:
#storing all the elem with the same anagram inside an array
#=> use the hashmap, key= the array of its char occurance; value = list of the word with same anagram
#for example: [1a 1c 1t]: ["act","cat"] => put them inside a hashmap
     

# [1a 1c 1t]: [act, cat]

hashmap=defaultdict(list)
res=[]

for string in strs:
    str_count= [0]*26

    for char in string:
        str_count[ord(char)-ord("a")]+=1
    
    hashmap[tuple(str_count)].append(string)

for val in hashmap.values():
    res.append(val)

return res

"""



'''
# [1a 1c 1t]: [act, cat]

def group_anagram(strs):
    hashmap=defaultdict(list)

    for s in strs:
        count_s=[0]*26
        for c in s:
            count_s[ord(c)-ord("a")]+=1
    
        hashmap[tuple(count_s)].append(s)
    
    return list(hashmap.values())

'''






















































