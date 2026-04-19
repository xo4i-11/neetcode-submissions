class TimeMap:

    def __init__(self):
        self.keyStore={} #key =string, value =[list of [value (string),timestamp (int)]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key]=[]
        self.keyStore[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        if key in self.keyStore:
            values=self.keyStore[key]
        else:
            values=[]
        
        #binary search (doable cuz the timstamp is in sorted order)
        l=0
        r=len(values)-1
        while l<=r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res=values[m][0]
                l= m+1
            else:
                r= m-1
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





