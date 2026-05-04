# https://leetcode.cn/contest/weekly-contest-500/problems/maximize-fixed-points-after-deletions/description/
# 2维偏序的LIS
# 为什么用a作为主排序？ 因为需要维护的LIS 需要满足 a 递增，
#  i-a 表示需要之前移除的数量，同时移除的数量也需要满足递增《= 这是LIS的要求，但是对于同一个值a，因为每个固定的值只能在LIS中出现一次，为了使得这个条件成立，把d大的放前面，
# 这样就能保证每个a值最多使得LIS长度增加1

from bisect import bisect_right,insort_left,bisect_left


class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        points = []
        for i, a in enumerate(nums):
            if 0 <= a <= i:
                points.append((a, i - a))

        points.sort(key=lambda x: (x[0], -x[1]))
        print(points)
        ls = []
        for _, d in points:
            idx = bisect_right(ls, d)
            if idx < len(ls):
                ls[idx] = d
            else:
                ls.append(d)    
        return len(ls)




re =Solution().maxFixedPoints([2,0,0])
print(re)