# https://leetcode.cn/problems/delete-duplicate-folders-in-system/submissions/645436381/?envType=daily-question&envId=2025-07-20
# 子树Hash，TrieTree 标记遍历
from typing import List, Tuple, Optional

dic = {}
class Trie:
    def __init__(self,val):
        self.children = {}
        self.isEnd =False
        self.val = val
        
    
    def insert(self,word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie(ch)
            node = node.children[ch]
        node.isEnd = False
    
    def dfsAndMark(self,node):
        cd = []
        #print(cd,node)
        for c in node.children:
            cd.append(self.dfsAndMark(node.children[c]))
        cd.sort()
        cdHsh = "$".join(cd)
        #print(node.val,cdHsh)
        if len(cd) > 0:
            if cdHsh not in dic:
                dic[cdHsh] =node
            else:
                dic[cdHsh].isEnd = True
                node.isEnd = True
        return "/" +node.val +"*"+cdHsh + "*"

    def dfs(self,node):
        ret =[]
        if node.isEnd == True:
            #print(node,node.isEnd)
            return ret 
        ret = [[node.val]]
        for c in node.children:
            #print(c,node.children,"x",node.children[c].isEnd)
            if node.children[c].isEnd == False:
                
                ct = self.dfs(node.children[c])
                #print(ct,"b")
                for x in ct:
                    ret.append([node.val] +x)
        return ret

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        global dic
        tri = Trie("??")

        dic = {}
        for ls in paths:
            tri.insert(ls)
        tri.dfsAndMark(tri)
        #print(dic)
        ret = []
        for a in tri.children:
            ret.extend(tri.dfs(tri.children[a]))
        return ret
        
paths =[["b"],["f"],["f","r"],["f","r","g"],["f","r","g","c"],["f","r","g","c","r"],["f","o"],["f","o","x"],["f","o","x","t"],["f","o","x","d"],["f","o","l"],["l"],["l","q"],["c"],["h"],["h","t"],["h","o"],["h","o","d"],["h","o","t"]]
paths = [["a"],["a","c"],["a","c","b"],["a","w"],["a","w","y"],["z","c"],["z","c","b"],["z","c","w"],["z","c","w","y"],["z"]]
re = Solution().deleteDuplicateFolder( paths )
print(re)