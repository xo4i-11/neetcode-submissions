class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #non empty array => dont need to check len(array)
        res=0 # (n XOR 0) = n

        for n in nums:
            res = res^n # ^ is XOR
        
        return res
        




"""
idea: 

 ex: [1,2,3,2,1]

1.

    1: ...0001
    2: ...0010
    3: ...0011
    2: ...0010
    1: ...0001

    => the thing above will be equivalent to:

2.  
    1: ...0001
    1: ...0001
    2: ...0001
    2: ...0001
    3: ...0011

3.

    when we XOR them:
    
    1: ...0001  }   0000
    1: ...0001  }

    2: ...0001  }
    2: ...0001  }   0000

    3: ...0011  }   0011


=> overall we should xor all of them toghter 
"""
        