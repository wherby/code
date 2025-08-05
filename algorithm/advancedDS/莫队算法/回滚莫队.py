# 用莫队求比较复杂的频率计算， 如果左右端点小于块值，先暴力计算
# 然后用莫队排序的方式，处理每个完整的起始端点，如果完整的起始端点不同，计数重置，对于完整起始端点到左断电的时候，先记录测量值，往左加，得到答案，然后退回完整起始点，重新恢复记录值
#
# https://www.bilibili.com/video/BV1p3h3zYEbc/?spm_id_from=333.1387.homepage.video_card.click&vd_source=ca787d3785cbd6247961eba27850fa0c
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from math import ceil,sqrt

class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(queries)

        cnt = defaultdict(int)
        max_cnt = min_val = 0

        # 添加元素 x
        def add(x: int) -> None:
            nonlocal max_cnt, min_val
            cnt[x] += 1
            c = cnt[x]
            if c > max_cnt:
                max_cnt, min_val = c, x
            elif c == max_cnt:
                min_val = min(min_val, x)

        ans = [-1] * m
        block_size = ceil(n / sqrt(m))

        qs = []  # (bid, ql, qr, threshold, qid) 其中 bid 是块号，qid 是询问的编号
        for i, (l, r, threshold) in enumerate(queries):
            r += 1  # 左闭右开

            # 大区间离线（保证 l 和 r 不在同一个块中）
            if r - l > block_size:
                qs.append((l // block_size, l, r, threshold, i))
                continue

            # 小区间暴力
            for x in nums[l: r]:
                add(x)
            if max_cnt >= threshold:
                ans[i] = min_val

            # 重置数据
            cnt.clear()
            max_cnt = 0

        qs.sort(key=lambda q: (q[0], q[2]))

        for i, (bid, ql, qr, threshold, qid) in enumerate(qs):
            l0 = (bid + 1) * block_size
            if i == 0 or bid > qs[i - 1][0]:  # 遍历到一个新的块
                r = l0  # 右端点移动的起点
                # 重置数据
                cnt.clear()
                max_cnt = 0

            # 右端点从 r 移动到 qr（qr 不计入）
            while r < qr:
                add(nums[r])
                r += 1

            tmp_max_cnt, tmp_min_val = max_cnt, min_val

            # 左端点从 l0 移动到 ql（l0 不计入）
            for x in nums[ql: l0]:
                add(x)
            if max_cnt >= threshold:
                ans[qid] = min_val

            # 回滚
            max_cnt, min_val = tmp_max_cnt, tmp_min_val
            for x in nums[ql: l0]:
                cnt[x] -= 1

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/threshold-majority-queries/solutions/3740919/mo-dui-suan-fa-hui-gun-mo-dui-pythonjava-x7yw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
