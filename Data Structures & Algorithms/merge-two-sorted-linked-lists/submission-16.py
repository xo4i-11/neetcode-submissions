# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1==None and list2==None:
            return 
        
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










"""
merge 2 sorted linkedlist:
we gonna use 2 ptr

ptr1 for list 1 and ptr2 for list 2

we iterate through every node in 2 array: while ptr1 and ptr2:
compare and add to a new linkedlist

if there still some extra node from either list1 or list2, append it to the linkedlist

"""


def merge(list1, list2):
    #edge:
    if list1 is None:
        return list2
    if list2 is None: 
        return list1
    
    curr1=list1
    curr2=list2
    dummy= ListNode(None, None)
    curr= dummy

    while curr1 and curr2:
        val1=curr1.val
        val2=curr2.val

        if val1< val2:
            curr.next=curr1
            curr1=curr1.next
            curr=curr.next
        
        else:
            curr.next=curr2
            curr2=curr2.next
            curr=curr.next
    
    if curr1:
        curr.next= curr1
    
    elif curr2:
        curr.next=curr2
    
    return dummy.next

            
































        
