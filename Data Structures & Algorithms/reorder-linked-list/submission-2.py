# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find the middle (when using fast slow 2 ptr, since fast travel x2 speed of slow => when fast reach end, slow at middle)
        slow= head
        fast= head


        while fast!=None and fast.next!=None:
            slow= slow.next
            fast= fast.next.next

        #reverse the right half
        right_prev=None #dummy node so that we can reverse
        right_curr= slow.next 
        slow.next=None #set the last_node.next in left node to None 


        while right_curr!=None:
            temp=right_curr.next
            right_curr.next= right_prev
            right_prev= right_curr
            right_curr=temp


        #merge 2 half
        first=head
        second= right_prev

        while second!=None:
            first_temp=first.next
            second_temp=second.next

            first.next=second
            second.next=first_temp

            first=first_temp
            second=second_temp

        return





    
    """

    #ideas:
    
        using fast slow 2 ptr

        #edge case: when head = None and head.next=None

        there are 3 main things we need to do:
            1. we find the middle node -> using fast slow 2 ptr

            2. reverse the order of right half
                first, we need to set the end_node.next of left half to none
                then, we reverse the right half ( careful about None )

            3. merge 2 half
                they gonna be in the final array 1 by 1 (1 from left, 1 from right; then keep doing that)
                loop until there is no node left in the right half
                add them 1 by 1

    """
        