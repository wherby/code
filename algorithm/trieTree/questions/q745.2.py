# https://leetcode.cn/problems/prefix-and-suffix-search/
from itertools import  zip_longest
class node:
    def __init__(self) -> None:
        self.child ={}
        self.idx =-1
        

class WordFilter:

    def __init__(self, words):
        self.root = node()
        for i ,word in enumerate(words):
            m = len(word)
            cur = self.root
            for j in range(m):
                a,b = word[j],word[m-1-j]
                tmp = cur
                for k in range(j,m):
                    key = (word[k],"#")
                    if key not in tmp.child:
                        tmp.child[key] = node()
                    tmp = tmp.child[key]
                    tmp.idx = i
                tmp = cur 
                for k in range(j,m):
                    key = ("#",word[m-1-k])
                    if key not in tmp.child:
                        tmp.child[key] = node()
                    tmp = tmp.child[key]
                    tmp.idx = i 
                if (a,b) not in cur.child:
                    cur.child[(a,b)] = node()
                cur = cur.child[(a,b)]
                cur.idx = i 
    
    def f(self, pref: str, suff: str) -> int:
        cur = self.root
        for key in zip_longest(pref, suff[::-1], fillvalue='#'):
            if key not in cur.child:
                return -1
            cur = cur.child[key]
        return cur.idx 
                        
            
        
        
re =WordFilter(["abbba","abba"])
print(re.f("ab","ba"))
