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
        head_of_right_half= slow.next
        dummy=None
        slow.next=None


        while head_of_right_half!=None:
            temp=head_of_right_half.next
            head_of_right_half.next=dummy
            dummy=head_of_right_half
            head_of_right_half=temp


        #merge 2 half
        first=head
        second= dummy

        while second!=None:
            first_temp=first.next
            second_temp=second.next

            first.next=second
            second.next=first_temp

            first=first_temp
            second=second_temp

        return








        



        



    
    """

    ideas: using fast slow 2 pointer

    EDGE CASE: when there is no head or no head.next


    1->6            1 6 2 5 
            2   5

    """
        