# https://leetcode.cn/problems/prefix-and-suffix-search/
class node:
    def __init__(self) -> None:
        self.child ={}
        self.ls=[]
        self.is_end = False
        
class TrieTree():
    def __init__(self) -> None:
        self.root =node()
    
    def insert(self,word,idx):
        cur = self.root
        for a in word:
            if a not in cur.child:
                cur.child[a] =node()
            cur = cur.child[a]
            cur.ls.append(idx)
        cur.is_end  =True
    
    def get(self,pre):
        cur = self.root
        for a in pre:
            if a not in cur.child:
                return []
            else:
                cur = cur.child[a]
        return cur.ls
class WordFilter:

    def __init__(self, words):
        self.tt= TrieTree()
        self.rtt = TrieTree()
        for i,word in enumerate(words):
            self.tt.insert(word,i)
            self.rtt.insert(word[::-1],i)
        
    def f(self, pref: str, suff: str) -> int:
        ls1 = self.tt.get(pref)
        ls2 = self.rtt.get(suff[::-1])
        idx1 = len(ls1)-1
        idx2  = len(ls2)-1
        while idx1 != -1 and idx2 !=-1:
            if ls1[idx1] < ls2[idx2]:
                idx2 -=1
            elif  ls1[idx1] >ls2[idx2]:
                idx1 -=1
            else:
                return ls1[idx1]
        return -1
        
re =WordFilter(["abbba","abba"])
print(re.f("ab","ba"))
