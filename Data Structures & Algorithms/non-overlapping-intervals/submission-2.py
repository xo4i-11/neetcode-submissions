class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # sort by end
        prev_end = float('-inf')
        count = 0 

        for i in range(len(intervals)):
            curr = intervals[i]
            curr_start = curr[0]
            curr_end = curr[1]

            #non overlap 
            if curr_start >= prev_end:
                prev_end = curr_end 
            #overlap
            else:
                count +=1
            
        return count

            

    




"""
problem:
    + given interval
    + return min num of intervals we need to remove to make the rest non-overlap


idea: USING GREEDY ALGO

- first, we should sort by end time because when two intervals overlap, keeping the interval     
 that ends earlier leaves more room for future intervals:
    + for example: we got [1,5] and [2,3] => Keep [2, 3] because it ends earlier. 
    Future intervals are more likely to fit after 3 than after 5. 
    
- Keeps the earliest-ending non-overlapping intervals.
- Removes every interval that conflicts with the last kept interval.


"""







"""
greedy: sort by the ending time, always prioritize the early-ended interval than the late-ended interval



"""
def non_overlapping(intervals):
    intervals.sort(key=lambda x:x[1])

    prev = intervals[0]
    count = 0

    for i in range(1, len(intervals)):
        prev_start = prev[0]
        prev_end = prev[1]

        curr = intervals[i]
        curr_start = curr[0]
        curr_end = curr[1]

        if prev_end <= curr_start:
            prev = curr
        else:
            count +=1

    return count  



















