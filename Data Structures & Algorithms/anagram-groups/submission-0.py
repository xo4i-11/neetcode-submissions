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