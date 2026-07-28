# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
            
        dummy = None

        prev = dummy
        curr = head 

        while curr: 
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        
        return prev 


    


"""
idea:

old:     0 -> 1 -> 2 -> 3 -> None
new:    None <- 0 <- 1 <- 2 <- 3 


"""
        