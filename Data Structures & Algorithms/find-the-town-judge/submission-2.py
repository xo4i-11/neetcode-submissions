class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_coming= defaultdict(int)
        out_going=defaultdict(int)

        for pair in trust:
            num1=pair[0]
            num2=pair[1]

            out_going[num1]+=1
            in_coming[num2]+=1
        
        for i in range(1,n+1):
            if in_coming[i]==n-1 and out_going[i]==0:
                return i
        
        return -1
        
        






    """
    idea: adj matrix
        + town just is trusted by everyone but doesn't trust anyone
        => the town judge have n-1 in-degree and 0 out-degree

        => we loop through every list in trust and assign the outgoing and ingoind edge

        finally, we check which one satisfy n-1 in-degree and 0 out-degree => judge


    """

        