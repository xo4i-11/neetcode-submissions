# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None:
            return

        #split in half: using fast slow 2 ptr
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #slow is currently the middle point
        #reverse the right half
        prev=None
        curr=slow.next
        slow.next=None

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        #merge 2 of them
        head_left=head
        head_right=prev

        while head_right:
            temp_left=head_left.next
            temp_right=head_right.next

            head_left.next=head_right
            head_right.next=temp_left

            head_left=temp_left
            head_right=temp_right
        
        return
        



        

        """
        ideas:
        [0, n-1, 1, n-2, 2, n-3, ...]

        => [0,1,2] -> None and [n-1,n-2,n-3] -> None
        => we will split it into 2 half, then reverse the right half. 
        after all the step, merge it 




        """

        