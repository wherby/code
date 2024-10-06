
## 双指针求同向值域


### 求刚好有k个就等价于 求多余k - 多余k+1
这个题目有两个现在 all(c[a]>0 for a in vowels) 和 c["_"] ==k 所以直接用双指针不能把两个特性（大于和等于）一起计算，
所以需要把等于的计算条件转换为大于的计算条件

N(K)= O(n>=k) - O(n>=(k+1))

https://leetcode.cn/contest/weekly-contest-417/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/

class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        def solve(w, k):
            c = Counter()
            j = 0
            z = 0
            for i in range(len(w)):
                if w[i] in 'aeiou':
                    c[w[i]] += 1
                else:
                    c['_'] += 1
                while c['a'] > 0 and c['e'] > 0 and c['i'] > 0 and c['o'] > 0 and c['u'] > 0 and c['_'] >= k:
                    if w[j] in 'aeiou':
                        c[w[j]] -= 1
                    else:
                        c['_'] -= 1
                    j += 1
                z += j
            return z
        return solve(w, k) - solve(w, k + 1)

## 求GCD刚好为k的对数

### 如果GCD为K 等于把公因数为K的数量减去所有nK(n>=2)的所有GCD的数量

```python
# https://leetcode.cn/problems/sorted-gcd-pair-queries/description/
# https://leetcode.cn/problems/sorted-gcd-pair-queries/solutions/2940421/er-fen-rong-chi-by-tsreaper-k5yq/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from bisect import bisect_right,insort_left,bisect_left



def getSubListUnderN(n):
    dic =defaultdict(set)
    visited=[[] for _ in range(n+2)]
    dic[1] = set([1])
    for i in range(2,n+1):
        if len(visited[i]):
            a = visited[i][0]
            k = i // a
            s =set(dic[k])
            t =set(s)
            for b in s:
                t.add(b*a) 
            dic[i] = t
            continue
        dic[i]=set([1,i])
        for j in range(i,n+1,i):
            visited[j].append(i)
    return dic

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        pdn = getSubListUnderN(mx+1)
        dic = defaultdict(int)
        c = defaultdict(int)
        for a in nums:
            for b in pdn[a]:
                c[b] +=1
        ## 求GCD为k 则为 等于把公因数为K的数量减去所有nK(n>=2)的所有GCD的数量
        ## 求值顺序从高到低
        for i in range(mx,0,-1):
            acc =c[i]*(c[i] -1) //2
            for j in range(2*i, mx+1,i):
                acc -= dic[j]
            dic[i] = acc
        pls =[0] 
        kd= {}
        for i,k in enumerate( sorted(dic.keys())):
            kd[i+1] =k 
            pls.append(pls[-1]+ dic[k])
        #print(pls,kd)
        ret =[]
        for b in queries:
            b+=1
            k = bisect_left(pls,b)
            ret.append(kd[k])
        return ret




re =Solution().gcdValues(nums = [2,3,4], queries = [0,2,2])
print(re)
```