"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # No meetings or only one meeting
        if len(intervals) <= 1:
            return len(intervals)

        # Process meetings in chronological order
        intervals.sort(key=lambda interval: interval.start)

        # Min heap stores the end time of every room currently in use
        rooms = []

        # First meeting always needs one room
        heapq.heappush(rooms, intervals[0].end)

        # Process remaining meetings
        for i in range(1, len(intervals)):
            meeting = intervals[i]

            # If the earliest finishing room is free,
            # reuse that room.
            if meeting.start >= rooms[0]:
                heapq.heappop(rooms)

            # Put this meeting into a room
            # (either reused or newly allocated)
            heapq.heappush(rooms, meeting.end)

        # Number of occupied rooms equals
        # minimum rooms required.
        return len(rooms)


    






"""
idea: 

    - we only need to care about When does this room become available again?
    => care only about the ending time 

    - we will use a minHeap to track the end interval time since:
        

                


"""
        