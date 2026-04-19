class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        charSet = set()
        res = 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                charSet.remove(s[l]) # REMOVE THE LEFT PTRRRRR
                l += 1
                
        return res


#remember we got a string of"abcabcbb" => we will need to check every possible substring 
#=> abc bca cab abc bc c b b 

"""
IDEAS:
we want a substring without duplicate elem => use set to track the seen element 

finding longest substring => we gonna use sliding window 
left ptr and right ptr both gonna start at index 0, we trynna traverse the right ptr until it reach the end of the string 
=> l=0,r=0
while r<len(s):

if the element is not in the set "seen", we gonna add it to seen and increase the count by 1

else if it is already in seen, we move the left ptr by 1( remember not to move right ptr) and check again with the condition above
ex: "zxyzxyz"
consider:
seen=(z,y,x)
streak=3
l=0, r=3
=> when r=3 => s[3]=z is in seen => it will be remove from seen => seen is now be (x,y) and l=1 
after that, we gonna run the loop again to check if s[r] (s[3]) is in seen or not. if not, then keep looping
"""

"""
l=0
r=0
res=0
seen=set()

while r<len(s):
    while s[r] in seen:
        seen.remove(s[r])
        l+=1
    seen.add(s[r])
    res=max(res,r-l+1)
    r+=1

return res
"""
    



































        

