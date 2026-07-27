class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key is None or value is None or timestamp is None:
            return 
        
        if key not in self.hashmap:
            self.hashmap[key] = []
        
        self.hashmap[key].append((value, timestamp))
        
        
    """
        idea:
            for get, return the value that is correspond to the key, the 


    """
    def get(self, key: str, timestamp: int) -> str:
        values = []
        if key in self.hashmap:
            values = self.hashmap[key]
        
        l = 0
        r = len(values) - 1

        res = ""
        #binary search to find the smallest possible val that 
        while l<=r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res=values[m][0]
                l=m+1
            else:
                r=m-1
        return res

        
    
#IDEAS:
#for get() function:
#   values = [
#      
#       ["a", 1],
#       ["b", 4],
#       ["c", 6],
#       ["d", 9]
#       
#       ]

# we wanna get('foo',7)
# => it should return c

        
