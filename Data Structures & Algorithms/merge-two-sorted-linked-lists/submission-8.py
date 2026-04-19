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
            list1 is head of list 1
            list2 is head of list 2


            create a dummy node so that dummy.next gonna be the head of the returned Linkedlist 
            we use 2 pointer, keep looping through 2 of them and compare.
            add it in the returned list

            if 1 one of them finished, point the end of the returned list to the rest of remaning one
        """
        
