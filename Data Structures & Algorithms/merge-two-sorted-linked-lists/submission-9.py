# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1==None and list2==None:
            return None
        
        if list1==None and list2:
            return list2
        
        if list2==None and list1:
            return list1

        dummy= ListNode(None,None)
        curr=dummy
        
        while list1 and list2:
            val1=list1.val
            val2=list2.val

            if val1 <= val2:
                curr.next=list1
                curr=curr.next
                list1=list1.next
            
            else:
                curr.next=list2
                curr=curr.next
                list2=list2.next
            
        
        if list1:
            curr.next=list1
        
        elif list2:
            curr.next=list2


        return dummy.next
                

        

            
    """
    Merge 2 sorted Linkedlist


    #NOT ACUTALLY POINTER, SINCE LINKEDLIST NODE IS ALREADY AN POINTER. WE RATHER THINK IT IN THE WAY OF A POINTER 
    i was thinking of using 2 pointer, 1 point to head of list 1 and other points to head of list 2 


    handle edge case:
    when 1 of them is empty => return the other one
    when both of them are empty => return None

    handle normal case, while both list is not None:
        compare ptr1 and ptr2:
            if ptr1<=ptr2: add p1 to the returned linkedlist, then move the poiner 
            else: add the ptr2 the linkedlist
        then add the rest of the pointer 2 in it


    """

        
