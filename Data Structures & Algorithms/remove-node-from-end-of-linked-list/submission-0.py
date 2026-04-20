# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==0:
            head=head.next
            return head
        
        track=1
        curr=head
        while track!=n:
            curr=curr.next
            track+=1
        
        if track-1==n:
            curr.next=None
            return head
        
        if curr.next!=None:
            temp=curr.next.next
            curr.next=temp
            return head

        
        
















    """
    ideas:
        we traverse to the node before the nth node
        temp=node.next.next
        node.next=temp
        

        #3 case:
        remove first, => return the node.next
        
        #remove middle => return head

        #remove last => return the head


        




    """