# https://leetcode.cn/contest/weekly-contest-525/problems/count-frequency-staircase-subarrays-ii/description/
# 使用 链表维护当前节点开始的最先出现的数字排序
# 使用惰性删除，只有需要检测下一个位置的时候才查询

class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        ixs = {}
        ix = {}
        i = n-1
        h = []
        r = 0
        class LK(object):
            def __init__(self, v, i):
                self.v, self.i = v, i
                self.n = None
        head = LK(0, -1)
        while i>=0:
            v = nums[i]
            if v not in ixs: ixs[v]=[]
            ixs[v].append(i)
            ix[v]=i
            nh = LK(v, i)
            nh.n = head.n
            head.n = nh
            k=1
            j = i
            ss = 0
            h = head
            while True:
                # find next accu
                while h.n:
                    ii, iv = h.n.i, h.n.v
                    if ix[iv]==ii: break
                    h.n = h.n.n
                if not h.n: break
                ii, iv = h.n.i, h.n.v
                h = h.n
                if len(ixs[iv])<k: break
                ss+=k
                j = max(j, ixs[iv][-k])
                if j-i+1==ss: r+=1
                k+=1
            i-=1
        return r