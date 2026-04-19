"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_arr=[]
        end_arr=[]

        for i in range(len(intervals)):
            start_arr.append(intervals[i].start)
            end_arr.append(intervals[i].end)
        
        start_arr.sort()
        end_arr.sort() 

        p1=0
        p2=0
        current=0
        max_room=0
        

        while p1 < len(start_arr):
            if start_arr[p1] < end_arr[p2]:
                current+=1
                p1+=1
                max_room=max(max_room,current)
                continue 
            
            else: 
                p2+=1
                current-=1
        
        return max_room
                



# 0, 5, 15
# 6, 10, 20
            
        
        


        
        




    """
    ideas: 
    we gonna create an array to store the start time (called start array)
    another array to store the end time (called end array)

    we will use 2 pointers, 1 point at the start array and another point at the end array.
    we will have a value to track the max meeting room and another to track the current meeting room

    we will loop through the start pointer. 
    if the start pointer < end pointer => current+=1, move the start pointer 

    else: current -=1, move the end pointer

    if the start array already finish (have loop through every elem), loop through the rest of the end array, => keep doing curr-=1
    """
        
    




    









        

        