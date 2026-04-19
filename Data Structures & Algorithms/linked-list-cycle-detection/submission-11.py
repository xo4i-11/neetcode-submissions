# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next       
            if slow == fast:
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





"""
Floyd's Cycle Detection Algorithm

we loop until the fast pointer reach null:

    slow ptr move 1 step
    fast pointer move 2 step
    if there is a cycle, they will catch up with each other 




"""

def optimized(head):
    slow= head
    fast= head
    
    while fast and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        
        if slow ==fast:
            return True
    
    return False
































