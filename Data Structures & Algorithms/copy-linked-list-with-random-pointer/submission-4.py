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
        #edge case
        if head is None or head.next is None:
            return head
        
        #create a hashmap, assign the None pair to it since 
        hashmap= {None: None}
        curr= head

        #create Node with val only, then create key:value pair
        while curr:
            copy_node= Node(curr.val, None, None)
            hashmap[curr]= copy_node
            curr=curr.next

        
        #start over from the beginning 
        curr= head

        #traverse through every copy node and assign the next, random ptr
        while curr:
            copy_node= hashmap[curr]
            copy_node.next= hashmap[curr.next]
            copy_node.random=hashmap[curr.random]
            curr= curr.next
        
        copy_head= hashmap[head]
        
        return copy_head
        


        
        """
        ideas:
        we wanna copy a similar linkedlist 

        i was thinking of storing in a hashmap such that the key is the node itself,
        the value would be a copy of that node but only store the value 

        traverse again 

        """









"""
question:
    - given the head of linkedlist size n
    - it has additional ptr called random, which may point to any node or null
    
    => we need to copy it 


idea:
    - we gonna use a hashmap such that: (we gonna traverse through the whole list to store)
        + key is the node itself
        + value is the node but only store the val (set the next and random ptr to Non)


    - we then traverse again to assign the next and random ptr 

"""

def copy(head):
    #edge case
    if head is None or head.next is None:
        return head
    
    #create a hashmap, assign the None pair to it since 
    hashmap= {None: None}
    curr= head

    #create Node with val only, then create key:value pair
    while curr:
        copy_node= Node(curr.val, None, None)
        hashmap[curr]= copy_node
        curr=curr.next

    
    #start over from the beginning 
    curr= head

    #traverse through every copy node and assign the next, random ptr
    while curr:
        copy_node= hashmap[curr]
        copy_node.next= hashmap[curr.next]
        copy_node.random=hashmap[curr.random]
        curr= curr.next
    
    copy_head= hashmap[head]
    
    return copy_head

    
    







































        