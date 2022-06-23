#如果插入数量不大的情况下，  不用合并range的情况更简单。。
#https://leetcode.cn/problems/falling-squares/
from bisect import bisect_right,bisect_left
class Solution:
    def fallingSquares(self, positions) :
        p, h, m = [0], [0], 0
        ans = []
        for x, y in positions:
            left = bisect_right(p, x)
            right = bisect_left(p, x+y)
            res = max(h[left-1:right]) + y
            p[left:right] = [x, x+y]
            h[left:right] = [res, h[right-1]]
            m = max(m, res)
            print(p,h)
            ans.append(m)
        return ans
    
re = Solution().fallingSquares([[1,2],[1,2],[2,3],[6,1]])
print(re)