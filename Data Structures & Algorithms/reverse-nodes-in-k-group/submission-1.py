# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group = 0
        curr = head

        # Count k nodes
        while curr and group < k:
            curr = curr.next
            group += 1
        
        if group != k:
            return head

        # If we have k nodes, reverse them
        curr = self.reverseKGroup(curr, k)

        while group > 0:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
            group -= 1

        head = curr   # ← must be OUTSIDE the loop

        return head
    

             
        
        






"""
question: 
- if the number of node < k => leave it there
- if the number of node >k:
    + recrusively reverse the rest of list first, then reverse the current 

=>SOVLE THE REST OF LIST FIRST, THEN FIX THE CURRENT GROUP


ideas:
    what we wanna return: head of the returned list

    #base case:
        first, we check if the first k nodes exist or not. if not, return head right the way

    if there exists at least k nodes:
        we gonna use recursion. we will keep reverse every k nodes after the first k nodes until there is n number of node left that is < k

    

"""