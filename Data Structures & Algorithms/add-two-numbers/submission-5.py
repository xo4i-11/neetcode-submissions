# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None

        dummy = ListNode(0, None)
        curr = dummy

        carry = 0    
        while l1 or l2 or carry != 0:
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:  
                val2 = l2.val
            else:
                val2 = 0

            total = val1 + val2 + carry

            carry = total // 10
            val = total % 10
            curr.next = ListNode(val, None)

            curr = curr.next
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        return dummy.next




        







        """
        3342 + 465

        5->6->4->0
        2->4->3->3

        7->0->8->3

        """

















        