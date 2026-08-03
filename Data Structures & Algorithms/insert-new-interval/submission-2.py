class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        res = []

        #sort by start time
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            insert_start = newInterval[0]
            insert_end = newInterval[1]

            # 1. Current interval is before newInterval.
            if curr_end < insert_start:
                res.append([curr_start, curr_end])

            # 2. Current interval is after newInterval 
            elif curr_start > insert_end:
                res.append(newInterval)

                # The remaining intervals are already sorted.
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                
                return res
            
            # 3. if overlap
            else:
                new_start = min(curr_start, insert_start)
                new_end = max(curr_end, insert_end)
                newInterval = [new_start, new_end]
        
        res.append(newInterval)
        return res

        

            
            

"""
problem:
    - insert the newInterval to intervals:
        + if they overlap, merge them
        + if not, they must be sorted by start_i ascending order

idea:
    - First, we sort the meeting by end time.
    - we loop through each meeting:
        + we figure out if the newInterval overlap with that or not, if yes => merge
        + if not, add to res

"""




def insert_interval(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]

    intervals.sort(key=lambda x:x[0])
    res = []

    insert_start = newInterval[0]
    insert_end = newInterval[1]

    for i in range(len(intervals)):
        curr = intervals[i]
        curr_start= intervals[i][0]
        curr_end = intervals[i][1]
        
        # case 1: if newInterval start before the old => add the new to res,
        # then add the rest to res
        if insert_end < curr_start:
            res.append(newInterval)

            for j in range(i, len(intervals)):
                res.append(intervals[i])
            
            return res
        
        #case 2: if the newInterval start after the curr:
        if insert_start > curr_end:
            res.append(curr)
        
        #case 3: else
        else:
            new_start = min(curr_start, insert_start)
            new_end = max(curr_start, insert_end)
            newInterval = [new_start, new_end]

        res.append(newInterval)
        return res        




















