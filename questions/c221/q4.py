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
                r= r.child[1-i]
            else:
                r = r.child[i]
        return r.max
    
    def __repr__(self):
        def recur(node, indent):
            return "".join(indent + str(key) + ("$" if ch and ch.is_end else "") + recur(ch, indent + "  ")  for key, ch in node.child.items())
        return recur(self.root, "\n")


class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums=sorted(nums)
        qs =[]
        for i, q in enumerate(queries):
            x,m = q[0],q[1]
            qs.append((m,x,i))
        qs = sorted(qs)
        idx =0
        trie = Trie()
        n = len(queries)
        res =[-1]*n
        for q in qs:
            m,x,i = q
            #print("q",q)
            tar = x ^((1<<32) -1)
            while idx <len(nums) and nums[idx]<=m:
                trie.insert(nums[idx])
                #print(nums[idx])
                idx +=1
            #print("cc",tar,'{:032b}'.format(tar),x)
            re = trie.get(tar)
            res[i] =re ^x if re !=-1 else -1
            #print(re,x,m,re ^x)
        #print(trie)
        return res

re =Solution().maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]])
print(re)