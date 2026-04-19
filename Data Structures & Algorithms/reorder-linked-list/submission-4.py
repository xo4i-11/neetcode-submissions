# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        #find the middle 
        #reverse the right half
        #merge

        #find middle: using fast slow 2 ptr
        slow=head
        fast=head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        #for now, the slow is currently at the middle and belongs to left half

        #seperate left half and create the right half
        right_curr=slow.next
        slow.next=None 
        prev=None

        #reverse the linkedlist
        while right_curr !=None:
            temp=right_curr.next
            right_curr.next=prev
            prev=right_curr
            right_curr=temp
        
        #l= 1 2 3 4 none
        #r= 7 6 5 none 
        # 1 7 2 6 3 5 4

        right_head=prev #7
        left_head=head #1

        while right_head!=None:
            temp_l = left_head.next # 2
            temp_r = right_head.next # 6

            left_head.next= right_head
            right_head.next= temp_l

            right_head=temp_r
            left_head= temp_l
        






    
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







    


























        