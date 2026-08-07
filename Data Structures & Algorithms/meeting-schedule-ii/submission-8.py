"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0  or len(intervals) ==1:
            return len(intervals)
        
        intervals.sort(key=lambda x:x.start)
        pq = []
        best = 0

        for interval in intervals:
            while pq and pq[0] <= interval.start:
                heapq.heappop(pq)
            heapq.heappush(pq, interval.end)
            best = max(best, len(pq))
        
        return best


    






"""
idea: 

    - we only need to care about When does this room become available again?
    => care only about the ending time 

    - we will use a minHeap to track the end interval time since:
        

                


"""
        