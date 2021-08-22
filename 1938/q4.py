from collections import defaultdict

from typing import List

class Trie:
    def __init__(self,*words):
        self.root =dict()
        for word in words:
            self.add(word)
    
    def add(self,word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter,dict())
        current_dict["_end_"] = True

    def __contains__(self,word):
        curent_dict= self.root
        for letter in word:
            if letter not in curent_dict:
                return False
            curent_dict = curent_dict[letter]
        return "_end_" in curent_dict
    
    ## find the nearest
    def find(self, word):
        current_dict = self.root
        res =""
        for letter in word:
            # TRY TO MATCH "1" TO "0" AND VICE VERSA
            desired = "1" if letter =="0" else "0"

            if not desired in current_dict: # if not match
                desired = letter  #set to sane
            res += desired
            current_dict = current_dict[desired]
        return res

    
    def delete(self,word):
        current_dict = self.root
        
        #nodes =[current_dict]
        objects = []
        for letter in word:
            current_dict = current_dict[letter]
            #nodes.append(current_dict)
            #print(current_dict)
            objects.append(current_dict)
        del current_dict["_end_"]

        #print(objects)
        #objects[:-1][::-1]) remove last one and reverse 
        #>>> a =[1,2,3]
        #>>> a[:-1]
        #[1, 2]
        #>>> a[:-1][::-1]
        #[2, 1]
        #>>> a
        #[1, 2, 3]
        for c, obj in zip(word[::-1],objects[:-1][::-1]):
            if not obj[c]:
                del obj[c]
            else:
                break

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        
        def makebin(x):
            return bin(x)[2:].zfill(5)
        
        query_node_to_query_list = defaultdict(list)
        for i,(node,val) in enumerate(queries):
            query_node_to_query_list[node].append((i,val))

        graph = defaultdict(list)

        for i,x  in enumerate(parents):
            graph[x].append(i)
        
        res =[-1 for _ in queries]

        t = Trie()

        def dfs(node):
            nodestr = makebin(node)
            t.add(nodestr)

            for i, val in query_node_to_query_list[node]:
                valstr = makebin(val)
                tagetstr =t.find(valstr)
                res[i] = int(tagetstr,2)^val
            
            for nex in graph[node]:
                dfs(nex)
            t.delete(nodestr)
        
        dfs(graph[-1][0])

        return res


parents = [3,7,-1,2,0,7,0,2]

queries = [[4,6],[1,15],[0,5]]
res = Solution().maxGeneticDifference(parents,queries)
print(res)