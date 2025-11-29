from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf



from math import ceil, log2
mod = 10**9+7
class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value 
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basev =0, basef=lambda x:x):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln>=l and rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        return self.merge( self._query_util( 2*i+1, ln, (ln+rn)//2, l, r ), self._query_util( 2*i+2, (ln+rn)//2+1, rn, l, r ) )

    def query(self, l, r):
        return self._query_util( 0, 0, self.n-1, l, r )

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v      

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        s3,s1 = "0",0
        cnt = 0
        pre = [(0,0)]
        ls = [0] 
        def merge(a,b):
            s1 = a +b 
            if s1 == "":
                return ""
            s1 = int(s1)%mod
            return str(s1)
        cur = 1
        for i,a in enumerate(s):
            if int(a) != 0:
                s1 +=int(a)
                c1 = int(a)
                ls.append(int(a))
                cnt +=1
            pre.append((cnt,s1))
        ret = []
        #ls.append("")
        print(ls)
        m = len(ls)
        cur = 1 
        for i,a in enumerate(ls[::-1]):
            ls[m-1-i] = a*cur%mod 
            cur = cur*10
         
        st = segment_tree(ls)

        print(pre,ls)
        for a,b in queries:
            p1,p2 = pre[a],pre[b+1]
            print(p1,p2)
            s1,s2 = p1
            c = st.query(p1[0]+1, p2[0])
            d = p2[1] -p1[1] 
            #print(c,d)
            ret.append(c*d%mod)
            print(a,b,c*d%mod,c,d)

        return ret
        



# s = "9223538386222334255"
# queries =[[0,0],[0,2],[0,3],[0,4],[0,5],[0,8],[0,9],[0,10],[0,11],[0,13],[0,16],[0,18],[1,1],[1,2],[1,3],[1,5],[1,7],[1,8],[1,12],[1,14],[1,16],[1,18],[2,3],[2,6],[2,9],[2,15],[2,16],[2,18],[3,3],[3,4],[3,6],[3,7],[3,8],[3,10],[3,15],[3,17],[4,8],[4,9],[4,11],[4,14],[4,16],[5,9],[5,11],[5,12],[5,16],[5,17],[5,18],[6,8],[6,17],[6,18],[7,8],[7,9],[7,10],[7,13],[7,14],[7,15],[7,16],[8,17],[8,18],[9,13],[10,10],[10,11],[10,13],[10,14],[10,15],[10,18],[11,14],[11,15],[12,15],[12,17],[13,14],[13,16],[13,17],[14,15],[14,18],[15,18]]

# re =Solution().sumAndMultiply(s , queries )
# exc = [81,11986,147568,1936935,22136472,661214761,953377757,4544034,753104778,226561370,510569189,632582266,4,88,1561,335295,58119958,760030492,765694238,600219323,101387995,714458248,115,494298,894458668,847108532,192236680,799326477,9,280,67222,778426,10615140,344586749,82273396,565636729,1453626,17766738,992029007,737983531,971468410,1074808,122835904,305131541,662150133,732534292,435670884,15922,866922629,780604232,418,6562,73378,100417798,120044750,745336938,177816025,22634492,338013363,933345,4,88,20007,266796,3557344,225359098,22330,312676,28008,4435075,198,40104,568225,238,650845,68080]
# print(re)
# print(exc)
# print(re==exc)




s = "83653355979889175588"
queries =[[0,2],[0,8],[0,10],[0,11],[0,13],[0,14],[0,15],[0,19],[1,4],[1,5],[1,6],[1,12],[1,16],[1,17],[1,18],[2,4],[2,5],[2,7],[2,9],[2,10],[2,11],[2,14],[2,19],[3,5],[3,7],[3,9],[3,10],[3,14],[3,15],[3,16],[4,9],[4,10],[4,15],[4,16],[4,18],[4,19],[5,6],[5,12],[5,14],[6,7],[6,8],[6,9],[6,10],[6,14],[6,15],[6,19],[7,9],[7,11],[7,13],[7,15],[7,17],[7,18],[8,8],[8,10],[8,12],[8,13],[8,18],[9,9],[9,10],[9,11],[9,13],[9,14],[9,15],[9,16],[9,19],[10,10],[10,14],[10,15],[10,19],[11,12],[11,19],[12,13],[12,16],[13,16],[13,17],[13,19],[14,14],[15,16],[15,17],[18,18]]

re =Solution().sumAndMultiply(s , queries )
exc = [14212,317077000,161389787,882329907,274699767,300940897,785430555,513914994,62101,730660,9133375,827275582,751358554,229370145,746249343,9142,111061,17640585,809430657,974510677,13585136,660746179,40897448,5863,1120455,197417089,454375020,305251240,238173859,279317386,10739104,137595139,251006020,409388971,764290238,568372898,280,922291345,827127435,550,10621,145522,1959265,147732113,663243696,545670509,12537,2272324,328893895,673301512,319067560,101983139,81,24475,4017508,48994450,157682279,49,1264,19152,3275449,33553422,391456933,314015422,688127163,81,3461185,41534514,463935280,1408,461359328,1513,2675250,201850,2477385,394550284,1,900,12835,64]

print(re)
print(exc)
print(re==exc)
print(int(s[:19+1])%mod)