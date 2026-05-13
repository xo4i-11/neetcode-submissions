class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        
        #sort the intervals by start time
        intervals.sort(key=lambda pair: pair[0])

        res=[]
        prev= intervals[0]

        for i in range(1,len(intervals)):
            curr= intervals[i] 

            curr_start=curr[0]
            curr_end=curr[1]
            prev_end=prev[1]

            if prev_end >= curr_start:
                new_end= max(prev_end, curr_end)
                prev[1]= new_end

            else:
                res.append(prev)
                prev=curr

        res.append(prev)
        return res
            



        
        



"""

def merge_intervals(intervals):
            
    if len(intervals)==0:
        return []
    
    intervals.sort (key=lambda pair: pair[0])
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


"""







































        