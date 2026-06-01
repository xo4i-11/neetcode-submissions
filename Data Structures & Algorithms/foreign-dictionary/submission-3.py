class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #init a hashmap: key = char, val = set store the value come after key
        adj_list = {}

        for word in words:
            for char in word:
                adj_list[char] = set()

        #loop through every words and compare each pair
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            
            #if w2 is the prefix of w1
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            #loop through every char to find the first diff char
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
        
        visited= {} #False = characted visited, True =  fvisited and in current path
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] =True

            for neighbor in adj_list[c]:
                if dfs(neighbor):
                    return True
            
            visited[c]=False
            res.append(c)
            return False

        for c in adj_list:
            if dfs(c):
                return ""
            
        res.reverse()
        return "".join(res)

                





"""
problem:
    - already sorted in lexicographical order based on rules of enw language
    - string a lexicographically smaller than b if:
        + letter of a < letter of b
        + a is prefix of b and a.length < b.length

idea: using Topological Sort



"""