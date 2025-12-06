# 贝格尔编排法 赛程 编排
# https://leetcode.cn/problems/generate-schedule/solutions/3781083/gou-zao-by-tsreaper-67y0/
# 主场队伍 i 需要和客场队伍 (i+1)modn，(i+2)modn，...，(i+n−1)modn 各赛一次，考虑对于固定值 j，把所有 i 和 (i+j)modn 的比赛放在一起按顺序编排。比如 n=5，j=2，
# 那就是 (0,2)，(1,3)，(2,4)，(3,0)，(4,1)。不难发现相邻比赛之间没有相同队伍，2≤j≤n−2 都可以这样编排。

# 但 j=1 和 j=n−1 有点麻烦。如果我们排成 (0,1)，(1,2)，...，那队伍 1 就连续比赛了。所以对于 j=1，我们只能排成 (0,1)，(2,3)，(4,0)，(1,2)，(3,4)。如果 n 是偶数，
# 比如 n=6，那就先枚举偶数主场队，再枚举奇数主场队，即 (0,1)，(2,3)，(4,5)，(1,2)，(3,4)，(5,1)。这样相邻比赛也没有重复队伍。

# 作者：TsReaper
# 链接：https://leetcode.cn/problems/generate-schedule/solutions/3781083/gou-zao-by-tsreaper-67y0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List, Tuple, Optional
class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <=4:
            return []
        ret = []
        for i in range(0,n,2):
            ret.append((i,(i+1)%n))
        for i in range(1,n,2):
            ret.append((i,(i+1)%n))
        
        def getBias(steps):
            for bias in range(n):
                x,y = bias,(bias+steps)%n 
                if x!=ret[-1][0] and x != ret[-1][1] and y !=ret[-1][0] and y != ret[-1][1]:
                    return bias

        for i in range(2,n-1):
            bias= getBias(i)
            for j in range(n):
                ret.append(((bias+j)%n,(bias+j+i)%n))
        
        bias = getBias(n-1)
        for i in range(0,n,2):
            ret.append(((bias + i)%n,(bias+i+n-1)%n))
        for i in range(1,n,2):
            ret.append(((bias + i)%n,(bias+i+n-1)%n))
        return ret



re = Solution().generateSchedule(5)
print(re)