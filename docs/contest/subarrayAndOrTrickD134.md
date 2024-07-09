
# DP feature on And Or operation
https://leetcode.cn/contest/biweekly-contest-134/

## Issue
如果没有利用子数组and/or性质[子数组and 利用了每个数字加入之后，以这个数字结尾的子数组的and的状态一定只有32个（数字位数决定）这一性质可以进行递推dp]，就会写出很繁琐的code

https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/description/

https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/submissions/536586719/

```
class Solution:
    def minimumDifference(self, nums: List[int], kk: int) -> int:
        ls= [deque([]) for _ in range(32)]
        for i,a in enumerate(nums):
            for j in range(32):
                if (1<<j)&a==0:
                    ls[j].append(i)
        mx =10**20
        
        for i in range(len(nums)):
            for j in range(32):
                while len(ls[j]) and ls[j][0] < i:
                    ls[j].popleft()
            dic = defaultdict(list)
            for j in range(32):
                if len(ls[j]):
                    dic[ls[j][0]].append(j)
            ks =list(dic.keys())
            ks.sort()
            acc =nums[i]
            #print(dic,acc)
            mx = min(mx,abs(acc-kk))
            for k in ks:
                for j in dic[k]:
                    if ((1<<j)&acc):
                        acc -= 1<<j
                mx = min(mx,abs(acc-kk))
                #print(acc,kk,i,k,mx)
        return mx
```

利用特性

```
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        pre= defaultdict(int)
        ans = inf
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            cur = defaultdict(int)
            cur[x]=1
            for key in pre.keys():
                cur[key|x] =1
                ans =min(ans, abs((key|x) - k))
            pre= cur
        return ans
```


https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/description/

https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/submissions/518495080/
```
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = 1,n
        if max(nums)>=k:
            return 1 
        acc = 0
        for a in nums:
            acc |=a 
        if acc <k:
            return -1

        pls = [[0]*32 ]
        for a in nums:
            acc = list(pls[-1])
            for i in range(32):
                if a &(1<<i):
                    acc[i] +=1
            pls.append(acc)
        #print(pls)
        def getN(acc):
            sm = 0
            for i in range(32):
                if acc[i]>0:
                    sm += 1<<i
            return sm
        def verify(mid):
            for i in range(mid,n+1):
                acc = [b-a for b,a in zip(pls[i],pls[i-mid])]
                if getN(acc) >=k:
                    return True
            return False
            
        while l < r:
            mid = (l+r)>>1
            if not verify(mid):
                l = mid +1
            else:
                r = mid
        return l if verify(l) else -1
```

利用特性

···
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ret = 10**10
        pre = {}
        for i,a in enumerate(nums):
            cur = defaultdict(int)
            pre[a] = i 
            for key,idx in pre.items():
                cur[key|a] = max(pre[key],cur[key|a] )
                if (key |a) >=k: 
                    ret = min(ret,i-cur[key|a]+1)
            pre = cur
        return ret if ret != 10**10 else -1
```


这个题目用前缀和和线段树也要超时
https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/description/

前缀和
https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/submissions/544567780/
```
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pls= [[0]*32 for _ in range(n+1)]
        for i,a in enumerate(nums):
            for j in range(32):
                if (1<<j)&a:
                    pls[i+1][j] =pls[i][j]+1
                else:
                    pls[i+1][j] =pls[i][j]
        sm =0
        @cache
        def get(s,e):
            tmp= 0
            for i in range(32):
                if pls[e+1][i]-pls[s][i] == e-s+1:
                    tmp+= 1<<i
            return tmp
        for i in range(n):
            l,r = i,n-1
            while l<r:
                mid = (l+r)>>1
                if get(i,mid)>k:
                    l = mid+1
                else:
                    r = mid
                #print("1")
            #print(get(i,mid),k,i,mid,"a")
            if get(i,l) != k :
                continue
            ll = l
            l,r = mid,n-1
            #print(l,r)
            while l <r:
                mid = (l+r+1)>>1
                #print(l,r,mid,'c')
                if get(i,mid)<k:
                    r= mid-1
                else:
                    l = mid
                #print(l,r,get(i,mid),mid,sm)
            sm += l-ll+1
            #print(i,sm,mid,ll,get(i,mid) ,"n")
        return sm
```
线段树
```
from math import ceil, log2

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basev = 0, basef=lambda x:x):
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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def count(nums):
            n = len(nums)
            sg = segment_tree(nums,merge=lambda a,b:a&b,basev=(1<<32)-1)
            sm= 0
            for i in range(n):
                l,r = i,n-1
                while l<r:
                    mid = (l+r)>>1
                    if sg.query(i,mid)>k:
                        l = mid+1
                    else:
                        r = mid
                    #print("1")
                #print(get(i,mid),k,i,mid,"a")
                if sg.query(i,l) != k :
                    continue
                ll = l
                
                sm += n-ll
                #print(i,sm,mid,ll,get(i,mid) ,"n")
            return sm
        sm = 0
        st=[]
        for a in nums:
            if a &k !=k :
                if len(st)!=0:
                    sm += count(st)
                st=[]
            else:
                st.append(a)
        if len(st):
            sm += count(st)
        return sm

```

利用特性
https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/submissions/544579649/
```
from collections import defaultdict,deque
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pre  = defaultdict(int)
        sm = 0
        
        for a in nums:
            cur = defaultdict(int)
            for key,v in pre.items():
                cur[key&a] +=v
            cur[a]+=1
            sm += cur[k]
            pre = cur
        return sm
```
### 

# https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/solutions/2833497/jian-ji-xie-fa-o1-kong-jian-pythonjavacg-u7fv/
# and or trick,在子数组中，以某个数组结尾的子数组，只有32个可能，而且前状态只能一个方向改变
#
from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        for i,x in enumerate(nums):
            for j in range(i-1,-1,-1):
                if nums[j]&x == nums[j]:
                    break
                nums[j] &= x 
            ans += bisect_right(nums,k,0,i+1) -bisect_left(nums,k,0,i+1)
        return ans