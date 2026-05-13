class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first, sort by starting time
        intervals.sort(key=lambda pair: pair[0])

        #init the retruned schedule, add the first interval and expand (merge) if needed 
        output=[intervals[0]]

        for start, end in intervals:
            last_end=output[-1][1]

            if start <= last_end:
                output[-1][1] = max(last_end,end)

            else:
                output.append([start,end])
        
        return output




                

        