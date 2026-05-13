class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first, sort by starting time
        intervals.sort(key=lambda pair: pair[0])

        res=[]

        prev= intervals[0]
        prev_start=prev[0]
        prev_end=prev[1]

        for i in range(1,len(intervals)):
            curr_start=intervals[i][0]
            curr_end=intervals[i][1]

            if curr_start <= prev_end:
                prev_end = max(prev_end, curr_end)
                prev = [prev_start, prev_end]
            
            else:
                res.append(prev)
                prev_start = curr_start
                prev_end= curr_end
                prev=intervals[i]
        
        res.append(prev)

        return res
            






                

        