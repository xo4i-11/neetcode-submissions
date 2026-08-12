# Node for doubly linkedlist
class Node:
    def __init__(self, key= None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # hashmap for caching. 
        # key = the key, value = Node(key, value)
        self.cache = {}

        #dummy node
        self.left= Node(0,0)
        self.right = Node(0,0)

        # use dummy node to form a doubly linked list: left <-> right
        self.left.next = self.right
        self.right.prev = self.left

    # remove a node from linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert a node to MRU postion 
    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right

        self.right.prev.next = node
        self.right.prev = node

    # whenever we get a key, we will need to update the location of it in cache
    def get(self, key: int) -> int:

        # key does not exist
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        #update new location
        self.remove(node)
        self.insert(node)

        return node.val

        
    def put(self, key: int, value: int) -> None:
        # if key already in cache
        if key in self.cache:
            # Remove old node from linked list
            self.remove(self.cache[key])
        
        insert_node = Node(key,value)
        self.cache[key] = insert_node

        self.insert(insert_node)

        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)

            del self.cache[lru_node.key]





        
        






"""
problem:
    - LRU Cache
    - get an put must be O(1)

idea:
    - since we need to find a key quickly (get must be O(1)) 
    => we use hashmap to store key, value pair 

    -  we use doubly linkedlist because it allows us to remove easier:
        for example: 
            +) A -> B -> C and we need to remove B 
            => we can do: B.prev.next = B.next
                          B.next.prev = B.prev
            
            +) if use singly, we need to know the the positon of A so that we can do:
                A.next = B.next



"""