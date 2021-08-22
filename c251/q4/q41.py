from typing import List

#https://leetcode.com/problems/delete-duplicate-folders-in-system/
from collections import defaultdict
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = {}
        child_hashes = defaultdict(list)

        for path in paths:
            node = tree
            for folder in path:
                if folder not in node:
                    node[folder] ={}
                node = node[folder]
        
        def dfs(node,node_key,parent):
            child_tuple = tuple(dfs(node[key],key,node) for key in sorted(node.keys()))
            #print(child_tuple)
            child_hash = hash(child_tuple)
            if child_tuple:
                child_hashes[child_hash].append((parent,node_key))
            return hash((child_hash,node_key))
        
        
        dfs(tree,None,None)
        #print(child_hashes)
        for duplicates in child_hashes.values():
            if len(duplicates) >1:
                for parent, node_key in duplicates:
                    del parent[node_key]
        #print(child_hashes)

        #print(tree)
        def dfs_collect_path(node,current,res):
            for key in node.keys():
                res.append(current + [key])
                dfs_collect_path(node[key],current + [key],res)
            return res
        return dfs_collect_path(tree,[],[])


a =Solution().deleteDuplicateFolder([["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]])
print(a)