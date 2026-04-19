class ListNode:
    def __init__(self,key):
        self.key=key
        self.next=None

class MyHashSet:

    def __init__(self):
        bucket_list=[]
        for i in range(10**4):
            bucket_list.append(ListNode(0)) # create buckets that start with dummy node (which is 0)
        self.set=bucket_list #set is just a name, can be anything

    def add(self, key: int) -> None:
        curr_position=key%len(self.set) #the bucket idx
        current_node = self.set[curr_position] # head of the linkedlist (the dummy node) a.k.a the first elem in the bucket
        while current_node.next != None:
            if current_node.next.key == key:
                return
            current_node=current_node.next
        current_node.next= ListNode(key)


    def remove(self, key: int) -> None:
        curr_position=key%len(self.set) 
        current_node = self.set[curr_position]
        while current_node.next != None:
            if current_node.next.key == key:
                current_node.next=current_node.next.next
                return
            current_node=current_node.next  

    def contains(self, key: int) -> bool:
        curr_position=key%len(self.set) 
        current_node = self.set[curr_position]
        while current_node.next != None:
            if current_node.next.key == key:
                return True
            current_node=current_node.next
        return False
        


"""IDEAS:

TECHNIQUE: CHAINING/LINKEDLIST 
( This technique was learned in CSE250, (near the Cuckoo hashing) where we create n bucket and split it into those bucket by (elem % n), 
and connect by linkedlist so that we can search inside the bucket for a specific node with the time of O(1))

So first, we gonna create a LinkedListNode class to connect the element with each other inside the bucket 

After that, for the construction of MyHashSet, we gonna create N buckets, each bucket is a linkedlist, 
store a DUMMY LINKEDLISTNODE first to avoid collosion and potential bug, we can append the node in the array afterwards

Visualize:
Buckets (array)
[   0,     1,       2,       3,      4,      5]
    |      |        |        |
 [dummy] [dummy]  [dummy]  [dummy] ....
    |
  [42]     ....
   ...



"""