# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        prev=None

        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            
        return prev

#link list: head->0->1->3->None
#Reverse: None<- 0 <-1 <- 3

#use 2 pointer 
# 1 to track the prev and 1 to track the current

#traverse through the whole linkedlist until reaching null to swap the arrow 


        







"""
0 -> 1 -> 2 -> 3 -> None
None <- 0 <- 1 <- 2 <- 3
"""

def reverse_linkedlist(head):
    if self.head is None:
        print("Empty")
        return None
    
    prev = None
    curr= head #0

    while curr is not None:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    
    return prev















"""
reverse a linkedlist:
    1-> 2-> 3->4-> None

    None <-1<-2<-3<-4
    l      r
           l  r       

return node 4
"""
def reverse_ll(head):
    if head is None:
        return None
    
    curr= head
    prev= None

    while curr:
        temp= curr.next
        curr.next=prev
        prev= curr
        curr=temp
    
    return prep




























