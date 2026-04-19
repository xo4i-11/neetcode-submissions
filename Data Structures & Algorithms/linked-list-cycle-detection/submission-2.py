# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        current=head
        seen=set()
        
        while(current is not None):
            if(current not in seen):
                seen.add(current)
                current=current.next
            else:
                return True
        return False
            










"""
#ideas:

we traverse through the map, track the occurance using set.
traverse, if meet => return false, else true





"""



def detect_cycle(head):
    curr=head
    seen=set()

    while curr:
        if curr in seen:
            return True
        
        seen.add(curr)
        curr=curr.next
    
    return False








































