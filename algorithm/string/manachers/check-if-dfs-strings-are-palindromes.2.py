# https://leetcode.cn/contest/weekly-contest-420/problems/check-if-dfs-strings-are-palindromes/
from typing import List, Tuple, Optional

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        def manachers(S):
            A = "@#" + "#".join(S) + "#$"
            Z = [0] * len(A)
            center = right =0
            for i in range(1,len(A)-1):
                if i < right:
                    Z[i] = min(right -i,Z[2*center -i]) # Z[2*center -i]是 i 关于center的对称点， 因为在[left, right]上对称，则 对称点的对称性是对称的
                while A[i + Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] +=1
                if i + Z[i] > right:
                    center,right = i , i+ Z[i]
            return Z[2:-2:1]
        n = len(s)
        ans = [None]*n

        time = 0
        g = [[] for _ in range(n)]
        for i,a in enumerate(parent):
            if a>=0:
                g[a].append(i)
        node = [[-1,-1] for _ in range(n)]

        def dfs(idx):
            nonlocal time 
            node[idx][0] = time
            for a in g[idx]:
                dfs(a)
            node[idx][1] = time 
            time +=1
        dfs(0)
        ls = ["*" for _ in range(n)]
        for i,(a,b) in enumerate(node):
            ls[b] = s[i]
        mls = manachers("".join(ls))
        for i,(a,b) in enumerate(node):
            ans[i] = mls[(a+b)]>=b-a
        return ans


re =Solution().findAnswer(parent = [-1,0,0,1,1,2], s = "aababa")
print(re)