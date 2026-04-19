class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res+=strs[0][i]

        return res



"""
ideas:
we gonna loop through every single character of the first string => for i in range (len(strs[0]))
we do the same for every other string (consider using many pointers point to the first char of every string) => for s in strs:

=> there is gonna be 2 case:
    if the first string is longer than the other: example: [flower,flow]
    => the common prefix is : flow => loop until i = len(flow)= len(s) => return the common prefix

    if they reach the character that does not have in common => return the common prefix
    ex: [bat,bag] => the common prefix is ba => loop until seeing that strs[0][i] != s[i]

if  everything is normal => res+=strs[0][i]

"""


"""
IDEAS: (NOT GOOD)
create  a variable to track the common prefix char

I am thinking of create a pointer for all of the elem and loop through every single string inside 
if we see that the len is too short, return 
if we see that there is a string that does not have common prefix => return
else, keep adding to the common prefix string

"""

def longest_common_prefix(strs):
    res="" 

    for i in range(len(strs[0])):
        for s in strs:
            if i==len(s) or strs[0][i]!=s[i]:
                return res
        
        res+=strs[0][i]

    return res
