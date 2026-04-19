"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy= {None: None} #handle the case when the random ptr point to None 

        curr=head
        while curr!=None:
            copy= Node(curr.val)
            old_to_copy[curr]=copy
            curr=curr.next
        

        curr=head
        while curr!=None:
            copy = old_to_copy[curr]
            copy.next=  old_to_copy[curr.next]
            copy.random= old_to_copy[curr.random]
            curr=curr.next
        
        return old_to_copy[head]






        
        






        """
        ideas: 
        want to copy a linked list that has next and random ptr.
        if we traverse through node and copy it, its not gonna work because there would be
        a case when the random pointer point to the node that haven't been visited yet 

        => create a hashmap with key= node and value = copy of that node( only store value)


        """
        