class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree = {}

        #init indegree of every char
        for word in words:
            for c in word:
                indegree[c] = 0
            
        #create adj list (graph) where:
        # key = node
        # val = that node's prerequisite
        graph = defaultdict(set)

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen= min(len(word1), len(word2))

            #invalid case: when w1=abc, w2=ab => return ""
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            #otherwise, comparing 2 words to build edge 
            for j in range(minLen):
                if word1[j] != word2[j]:
                    #avoid duplicate
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] +=1
                    break
        

        #kahn algo:
        # enqueue all nodes with indegree = 0
        queue = deque()
        res=[]


        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        while queue:
            node = queue.popleft()
            res.append(node)

            for neigh in graph[node]:
                indegree[neigh] -=1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        #cycle check
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)



            

 



                





        


        
        






"""
problem:
    - order of letter unknown
    - list of string: words; strings are sorted lexicographically 
    => return a string of unique letter in alien language 
    sorted in increasing order by new language rule. If multiple solution, return ANY of them
    If cannot correspond to any order of letters => return ""



approach:
    - since a letter with smaller lexicographically order must come before a letter with higher 
    to form a valid string (form a DIRECTED GRAPH) => we must use TOPOLOGICAL SORT
    
idea: TOPOLOGICAL SORT
    - compute in-degree for all nodes (nodes are the character):
        ex: "abc" and "abd" => c < d => graph[c] = d => indegree[d] = 1

    - build graph, comparing 2 words that stand next to each other:
        + if the longer word comes before its prefix => return ""
            * ex: w1 = abc, w2 = ab => return ""
        + Otherwise, add to adj list
    

"""