# https://leetcode.cn/contest/weekly-contest-496/problems/minimum-operations-to-achieve-at-least-k-peaks/
# /code/algorithm/linklist/链表的反悔贪心/虚拟节点的生成.md
import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k > n // 2:
            return -1
        c = [max(0, max(nums[(i-1) % n], nums[(i+1) % n]) + 1 - nums[i]) for i in range(n)]
        l = [(i-1) % n for i in range(n)]
        r = [(i+1) % n for i in range(n)]
        h = [(c[i], i) for i in range(n)]
        d = [False] * n
        heapq.heapify(h)
        ans = 0

        v = c[:]
        for _ in range(k):
            while True:
                cost, i = heapq.heappop(h)
                if not d[i]:
                    break
            ans += cost
            left, right = l[i], r[i]
            if left == right:  ## 这时左右点都是一个点了，再进行合并就错误了
                d[left] = d[i] = True
                continue   

            nv = v[left] + v[right] - cost
            ni = len(v)
            v.append(nv)
            l.append(l[left])
            r.append(r[right])
            d.append(False)

            r[l[left]] = ni
            l[r[right]] = ni

            d[left] = d[i] = d[right] = True
            heapq.heappush(h, (nv, ni))
        return ans