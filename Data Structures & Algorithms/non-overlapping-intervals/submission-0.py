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


idea:
- first, we should sort by end time because when two intervals overlap, keeping the interval     
 that ends earlier leaves more room for future intervals:
    + for example: we got [1,5] and [2,3] => Keep [2, 3] because it ends earlier. 
    Future intervals are more likely to fit after 3 than after 5. 
    
- Keeps the earliest-ending non-overlapping intervals.
- Removes every interval that conflicts with the last kept interval.

"""