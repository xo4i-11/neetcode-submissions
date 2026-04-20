class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        
        intervals.sort
        current_interval=intervals[0]
        res=[]

        for i in range(1,len(intervals)):
            if intervals[i][0] <= current_interval[1]:
                current_end=max(current_interval[1],intervals[i][1])
                current_interval=[current_interval[0],current_end]
            else:
                res.append(current_interval)
                current_interval=intervals[i]
        
        res.append(current_interval)
        return res

    













        