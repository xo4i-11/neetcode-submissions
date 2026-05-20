class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i=0
        hashmap={}
        for c in order:
            hashmap[c]=i
            i+=1

        for j in range(len(words)-1):
            word1=words[j]
            word2=words[j+1]

            for k in range(len(word1)):
                if k == len(word2):
                    return False
                
                if word1[k]!=word2[k]:
                    if hashmap[word1[k]] > hashmap[word2[k]]:
                        return False
                    break
            
        return True

        




"""
problem: verify that for each words, the character of that word must come after the character of prev word
with the same idx in alien dictionary

for example:
    Input: words = ["dag","disk","dog"], order = "hlabcdefgijkmnopqrstuvwxyz"

    we now compare 2 word at a time:
    - dag vs disk: d=d, a<i => true
    - disk vs dog: d=d, i<o => true
    => TRUE

another example:
    Input: words = ["he", "hello"] => True (the shorter letter must come first)

    in other word, if word A is prefix of word B, word B must be after word A

"""

"""
idea:
    - put every letter of the "order" into a hashmap where: key=c value=idx 
    
    - compare 2 word at a time => we loop through every word
        + we get 2 word:
            loop through every index of that 2 word and compare:
                + if we already loop through every char of word2 => len(word1)>len(word2) =>false
                + if the char1 != char2 and order of char 1 > order of char 2 => false

    
"""