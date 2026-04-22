# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None

        dummy = ListNode(0, None)
        curr = dummy

        carry = 0    
        while l1 or l2 or carry != 0:
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:  
                val2 = l2.val
            else:
                val2 = 0

            total = val1 + val2 + carry

            carry = total // 10
            val = total % 10
            curr.next = ListNode(val, None)

            curr = curr.next
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        return dummy.next




        """
        3342 + 465

        5->6->4->0
        2->4->3->3

        7->0->8->3

        """


"""
idea: 
    - Basic conception:since the question already reverse the 2 linkedlist => use the 2 ptr and add them up
    
    - To implement:
        + create 2 ptr, 1 start from l1 and 1 start from l2
        + create a variable: carry (to track the remaining of a sum)
    
    - First, we use 2 ptr and move through both linkedlist.
    - if the sum of 2 variable > 10 => add 1 and check if there is any carry or not
"""


def add_2_num(l1, l2):
    #edge case
    if l1 is None and l2 is None:
        return None

    if l1 is None:
        return l2

    if l2 is None:
        return l1

    #use 2 ptr and move them till reaching the end
    ptr1= l1
    ptr2= l2

    #track the remaining of sum
    carry=0

    #create dummy to assign node to returned linkedlist
    dummy= ListNode(None, None)
    curr= dummy

    while ptr1 or ptr2 or carry!=0:
        #check if there is any num at ptr1
        val1= 0
        if ptr1:
            val1= ptr1.val
        
        #check if there is any num at ptr2
        val2=0
        if ptr2:
            val2= ptr2.val

        #the sum of that col
        total = val1 + val2 + carry

        #create the node and assign to returned linkedlist
        new_node_val= total%10
        carry= total//10
        
        new_node=ListNode(new_node_val, None)
        curr.next= new_node
        curr= curr.next

        #update the postion of ptr1 and ptr2
        if ptr1:
            ptr1=ptr1.next
        
        if ptr2:
            ptr2=ptr2.next
    
    return dummy.next

        

        
        

        

        

        













        