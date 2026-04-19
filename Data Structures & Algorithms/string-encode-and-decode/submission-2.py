class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+= str(len(s)) + "#" +s
        return res

    def decode(self, s: str) -> List[str]:
        res=[] 
        i=0 #i is to track the current index

        while(i<len(s)):
            j=i
            while(s[j]!="#"): #we need this since there might be 2 digit numbers ex:10#leettttttt
                j+=1    #j is used to bound the char that not gonna be in the res( ex: j bound till: 10#)
            length=int(s[i:j])
            res.append(s[j+1: j+1+length])
            i=j+1+length
        return res

#"4#leet5#co#de" 

#Constraints: there is no limit of the character (it can be any character on the keyboard)
#example: ["leet","co#de"] -> encode: "leetco#de" -> decode: ["leet", "co#de"]

#IDEAS:
#after encoding, we want to transfer 4 first char to "leet", and 5 next char to "co#de"

#we gonna store an int at the beginning of every string, follow with a # to tell us that we gonna read 4 char after the #
#ex: 4#neet5#co#de
#=> read 4 char after the # (which is neet)
#=> read 5 char after the # (which is co#de)

#=> for encode: we read and add the length of the string
#add the # after that number
#add the string 

#=> for decode: we create 1 ptr to track the the current location and another to bound the number to get the length
#use slicing to add it to the res

"""

def encode(self, strs: List[str]) -> str:
    res=""
    for s in strs:
        res+= str(len(s))+"#"+s
    return res


def decode(self, s: str) -> List[str]:
    res=[]
    i=0
    #"4#neet5#co#de"
    while i< len(s):
        j=i
        while s[j]!="#":
            j+=1
        length=int(s[i:j])
        res.append(s[j+1:length+j+1])
        i=length+j+1
    return res



#encode a list of string to a string 
#=> encode so that the ["Hello","World"] => 5#Hello5#World

def encode(strs):
    res=""
    for string in strs:
        res+= len(str) + "#" + string
    return res

#4neet5#co#de
def decode(s):
    res=[]
    i=0 #track the current idx
    while i<len(s):
        j=i
        while s[j]!="#":
            j+=1
        length=int(s[i:j])
        res.append(s[j+1:length+j+1])
        i=length+j+1
    return res

"""









































    
    









    