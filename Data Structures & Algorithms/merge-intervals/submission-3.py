class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        
        intervals.sort(key=lambda x: x[0])

        curr_inter=intervals[0]
        curr_start=curr_inter[0]
        curr_end=curr_inter[1]
        res=[]

        for i in range(1,len(intervals)):
            next_start=intervals[i][0]
            next_end=intervals[i][1]

            if curr_end >= next_start:
                cu_end = max(curr_end,next_end) 
                curr_inter= [curr_start,cu_end]
            
            else:
                res.append(curr_inter)
                curr_inter=intervals[i]
                curr_start=curr_inter[0]
                curr_end=curr_inter[1]

        res.append(curr_inter)
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







































        