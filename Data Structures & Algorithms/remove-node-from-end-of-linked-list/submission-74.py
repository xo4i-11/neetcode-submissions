# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None 
        
        dummy = ListNode(None, head)
        slow = dummy
        
        fast = head
        for i in range(n):
            fast = fast.next
        
        while fast != None:
            slow = slow.next
            fast = fast.next


        slow.next = slow.next.next

        return dummy.next            
        



        