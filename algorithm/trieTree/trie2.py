#//questions/c221/q4.py #https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array/
from math import inf

class node:
    def __init__(self) -> None:
        self.child ={}
        self.max =-inf
        self.min = inf
        self.is_end = False

class Trie:
    def __init__(self) -> None:
        self.root = node()
    
    def insert(self,w):
        ls = '{:032b}'.format(w)
        r = self.root
        for i in ls:
            i = int(i)
            if i not in r.child:
                r.child[i] = node()
            r = r.child[i]
        r.max = max(r.max,w)
        r.min = min(r.min,w)
        r.is_end = True
    
    def get(self,x):
        r =self.root
        if len(r.child) == 0:
            return -1
        ls = '{:032b}'.format(x)
        for i in ls:
            i = int(i)
            if i not in r.child:
                print(r.child,1-i)
                r= r.child[1-i]
            else:
                r = r.child[i]
        return r.max
    
    def __repr__(self):
        def recur(node, indent):
            return "".join(indent + str(key) + ("$" if ch and ch.is_end else "") + recur(ch, indent + "  ")  for key, ch in node.child.items())
        return recur(self.root, "\n")