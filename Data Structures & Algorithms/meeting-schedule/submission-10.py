"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        if len(intervals) == 0:
            return True
        
        prev = intervals[0]

        for i in range(1, len(intervals)):
            prev_start = prev.start
            prev_end = prev.end

            curr = intervals[i]
            curr_start = curr.start
            curr_end = curr.end

            if curr_start < prev_end:
                return False
            
            else:
                prev = curr
            
        return True
            

