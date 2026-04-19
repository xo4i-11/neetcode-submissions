# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        dummy=ListNode()
        curr=dummy
        
        while (list1 and list2) is not None:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            
            else:
                curr.next=list2
                list2=list2.next
            
            curr=curr.next
        
        if list1:
            curr.next=list1
        elif list2:
            curr.next=list2
        
        return dummy.next



#IDEAS:
#list1 represent the head of list 1
#list2 represent the head of list 2
#create a dummy node, which will represent the head of a new linkedlist that we wanna return and traverse it
#we gonna keep comparing the 2 val in the 2 linkedlists and added to the returned linkedlist
#ex: output->dummy->1->1->2->3->4









"""
Merge 2 sorted Linkedlist

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


    

















































