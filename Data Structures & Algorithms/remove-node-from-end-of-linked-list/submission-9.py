# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        
        l=dummy
        r=head
        
        for i in range(n):
            r=r.next
        
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

        1 -> 2 -> 3 -> 4 -> None

        if we remove 3:
        
        1 -> 2 -> 4 -> None

        #idea is to create dummy node at beginning and slide the window of size n since:
            if we dont make a dummmy node:

                1 -> 2 -> 3 -> 4 -> None
                l         r 

                if we move till the end => we could not remove the elem since the left ptr is pointer at the elem.
                    1 -> 2 -> 3 -> 4 -> None
                              l           r


            if we do make a dummy node

            0 -> 1 -> 2 -> 3 -> 4 -> None
            l              r

                if move till end;
                 0 -> 1 -> 2 -> 3 -> 4 -> None
                           l                r

                => we can remove node 3 by setting 2.next=2.next.next 
    """


