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
        







        """"
        if they traverse in a cycle -> they will meet each other 
        => we will use fast slow 2 ptr

        """
        def cycle_detect(head):
            slow=head
            fast=head

            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    return True
            
            return False