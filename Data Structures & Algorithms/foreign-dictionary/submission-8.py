class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create a graph and in-degree
        adj = defaultdict(set)
        indegree = {}

        #init all char
        for word in words:
            for c in word:
                indegree[c]=0

        #build edge
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen= min(len(w1), len(w2))

            #invalid case: prefix issue:
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            #loop through char in word and compare
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]: #avoid duplicate
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break
            

        #Kahn algo
        queue=deque()
        res=[]
        
        #in kahn algo, we add all node with indegree=0 to the queue
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        while queue:
            c = queue.popleft()
            res.append(c)
            
            for neighbor in adj[c]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        
        #cycle check:
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)






        



"""
problem:
    - already sorted in lexicographical order based on rules of enw language
    - string a lexicographically smaller than b if:
        + letter of a < letter of b
        + a is prefix of b and a.length < b.length

idea: using Topological Sort

"""


def diction(words):
    # we wanna store: key = unique char and val = its neighbor
    # => it represent the edge (from:key to:value)
    adj = defaultdict(set)
    indegree = {}

    #init the indegree
    for word in words:
        for c in word:
            indegree[c]=0

    #form the edge by comparing 2 adj words together
    for i in range(len(words)-1):
        w1 = words[i]
        w2 = words[i+1]
        minLen= min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[0:minLen] == w2[0:minLen]:
            return ""
        
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                indegree[w2[j]]+=1
    
    return


    


















