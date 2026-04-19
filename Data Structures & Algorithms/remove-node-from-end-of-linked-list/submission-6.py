# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(0,head)
        l=dummy

        r=head
        for i in range(n):
            r=r.next
        
        #left currently at dummy
        #right currently at nth node from start

        while r!=None:
            l=l.next
            r=r.next
        
        l.next= l.next.next
        return dummy.next
   

    
        
        
















    """
        ideas:

        we wanna remove the Nth node from the end of linkedlist
        we gonna use fixed size 2 ptr
        we create a dummy node; left start at dummy node
        r start at Nth node from the beginning 
        => we keep sliding the window until right reach null 
        if right reach null, left reach the target


        




    """