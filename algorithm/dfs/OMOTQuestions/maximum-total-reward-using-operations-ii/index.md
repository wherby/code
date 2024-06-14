# 
https://leetcode.cn/contest/weekly-contest-401/problems/maximum-total-reward-using-operations-ii/description/
## DP 优化

https://leetcode.cn/contest/weekly-contest-401/problems/maximum-total-reward-using-operations-ii/submissions/538225809/
如果直接查找会超时 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        acc =rewardValues[-1]
        ls = rewardValues[:-1]
        sl = SortedList([i for i in range(1,acc)])
        dic= {}
        dic[0] =1
        for a in ls:
            l = sl.bisect_left(a)
            r = min(sl.bisect_left(a*2-1),len(sl)-1)
            rm =[]
            for i in range(l, r+1):
                if sl[i] -a in dic and sl[i]-a <a:
                    rm.append(sl[i])
            for a in rm:
                sl.remove(a)
                dic[a] =1
            #print(a,dic)
        for i in range(acc-1,-1,-1):
            if i in dic:
                return acc+i


使用单调队列优化candidate值

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

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        acc =rewardValues[-1]
        ls = rewardValues[:-1]
        ls = set(ls)
        ls = list(ls)
        ls.sort()
        sl = SortedList([])
        dic= {}
        dic[0] =1
        lst =0
        for a in ls:
            for i in range(max(a,lst),2*a):
                sl.add(i)
            #print(sl,a)
            rm = []
            l = 0
            while l < len(sl) and sl[l]<a:
                rm.append(sl[l])
                l+=1

            for b in rm:
                sl.remove(b)
            lst =a*2-1
            rm = []
            
            for j in sl:
                if j-a in dic:
                    dic[j] =1
                    rm.append(j)
            
            for b in rm:
                sl.remove(b)
            #print(sl,dic)
        for i in range(acc-1,-1,-1):
            if i in dic:
                return acc+i




re =Solution().maxTotalReward(rewardValues =  [2,17,12])
print(re)

## Using long bit function in python lib



class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        f = 1
        for v in sorted(set(rewardValues)):
            f |= (f & ((1 << v) - 1)) << v
        return f.bit_length() - 1


        
https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/solutions/2805413/bitset-you-hua-0-1-bei-bao-by-endlessche-m1xn/

对于 rewardValues\textit{rewardValues}rewardValues 中的数，如果先选大的，就没法再选小的，所以按照从小到大的顺序选是最好的。

把 rewardValues\textit{rewardValues}rewardValues 从小到大排序。

排序后，问题变成一个标准的 0-1 背包问题，请看【基础算法精讲 18】。

对于本题，定义 f[i][j]f[i][j]f[i][j] 表示能否从前 iii 个数中得到总奖励 jjj。

考虑 v=rewardValues[i]v=\textit{rewardValues}[i]v=rewardValues[i] 选或不选：

不选 vvv：f[i][j]=f[i−1][j]f[i][j] = f[i-1][j]f[i][j]=f[i−1][j]。
选 vvv：f[i][j]=f[i−1][j−v]f[i][j] = f[i-1][j-v]f[i][j]=f[i−1][j−v]，前提是 j≥vj\ge vj≥v 且 j−v<vj-v < vj−v<v，即 v≤j<2vv\le j<2vv≤j<2v。
满足其一即可，得

f[i][j]=f[i−1][j]∨f[i−1][j−v]f[i][j] = f[i-1][j] \vee f[i-1][j-v]
f[i][j]=f[i−1][j]∨f[i−1][j−v]
其中 ∨\vee∨ 即编程语言中的 ||。

初始值 f[0][0]=truef[0][0] = \texttt{true}f[0][0]=true。

答案为最大的满足 f[n][j]=truef[n][j]=\texttt{true}f[n][j]=true 的 jjj。

这可以解决周赛第三题，但第四题范围很大，需要去掉第一个维度，并用 bitset 优化。

用一个二进制数 fff 保存状态，二进制从低到高第 jjj 位为 111 表示 f[j]=truef[j]=\texttt{true}f[j]=true，为 000 表示 f[j]=falsef[j]=\texttt{false}f[j]=false。

对于上面的转移方程 f[i][j]=f[i−1][j]∨f[i−1][j−v]f[i][j] = f[i-1][j] \vee f[i-1][j-v]f[i][j]=f[i−1][j]∨f[i−1][j−v]，其中 0≤j−v<v0\le j-v < v0≤j−v<v，相当于取 fff 的低 vvv 位，再左移 vvv 位，然后与 fff 取按位或。

初始值 f=1f=1f=1。

答案为 fff 的最高位，即 fff 的二进制长度减一。

代码实现时，可以把 rewardValues\textit{rewardValues}rewardValues 中的重复数字去掉，毕竟无法选两个一样的数。

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/solutions/2805413/bitset-you-hua-0-1-bei-bao-by-endlessche-m1xn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。