class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            n = n & n-1
            count+=1
        
        return count 




    


"""
problem:
    unsigned int n: number that >= 0
    return number of 1 bits

idea:
    ex: n= 11 => bit: 1011
        n= 10 => bit: 1010
        we do 10&11 => 1010 (=> get rid one of the number 1)
        
        n= 10 => bit = 1010
        n= 9  => bit = 1001
        we do 9&10 => 1000 (=> get rid one more number 1 )

        n=9 => bit = 1000
        n=8 => bit = 0100
        we do 9&8 => 0000 (=> get rid one more number 1)

        => OVERALL GET RID OF 3 NUMBER 1
        => COUNT = 3

        FORMULA: n & (n-1)

"""
        