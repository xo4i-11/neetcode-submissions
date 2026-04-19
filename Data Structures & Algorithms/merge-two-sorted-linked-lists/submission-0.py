# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode()
        curr=dummy

        while(list1 and list2): #while list 1 and list 2 not none
            if list1.val <list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            
            curr=curr.next

        if(list1):
            curr.next=list1
        elif(list2):
            curr.next=list2
            
        return dummy.next


#IDEAS:
#create a dummy node, which will represent the head of a new linkedlist that we wanna return and traverse it
#we gonna keep comparing the 2 val in the 2 linkedlists and added to the returned linkedlist
#ex: output->dummy->1->1->2->3->4
