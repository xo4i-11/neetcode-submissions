class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals.copy()

        intervals.sort(key=lambda x:x[0])

        prev = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            prev_start = prev[0]
            prev_end = prev[1]

            curr = intervals[i]
            curr_start = curr[0]
            curr_end = curr[1]
            
            #overlap
            if curr_start <= prev_end:
                prev_new_end = max(curr_end, prev_end)
                prev = [prev_start, prev_new_end]

            #non-overlap
            else:
                res.append(prev)
                prev = curr
        
        res.append(prev)
        return res







        