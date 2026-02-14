from collections import Counter
from math import inf

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        cnt = Counter(s)
        if max(cnt.values()) * len(cnt) == n:  # s 是平衡的
            return n

        mp = {c: i for i, c in enumerate(cnt)}
        s = [mp[c] for c in s]  # 离散化，字母 -> 数字

        n = len(s)
        suf_orders = [None] * n
        order = []
        for i in range(n - 1, -1, -1):
            # 把最近出现的字母移到 order 末尾
            try: order.remove(s[i])
            except: pass
            order.append(s[i])
            suf_orders[i] = order[:]

        order = []
        cnt = [0] * len(mp)
        pos = {}
        ans = 0
        for i, b in enumerate(s):
            suf_order = suf_orders[i]
            min_ch = inf
            mask = 0
            for j in range(len(suf_order) - 1, -1, -1):
                min_ch = min(min_ch, suf_order[j])
                # 注意此时 cnt 并不包含 s[i]，我们计算的是前缀 s[:i] 的信息
                # 在子串中的字母，计算差值
                # 不在子串中的字母，维持原样
                d = cnt[:]
                for ch in suf_order[j:]:
                    d[ch] -= cnt[min_ch]
                mask |= 1 << suf_order[j]
                p = (tuple(d), mask)  # mask 用来区分 d[ch] 是差值还是原始值
                # 记录 p 首次出现的位置
                if p not in pos:
                    pos[p] = i - 1

            # 把最近出现的字母移到 order 末尾
            try: order.remove(b)
            except: pass
            order.append(b)

            cnt[b] += 1
            min_ch = inf
            mask = 0
            for j in range(len(order) - 1, -1, -1):
                min_ch = min(min_ch, order[j])
                d = cnt[:]
                for ch in order[j:]:
                    d[ch] -= cnt[min_ch]
                mask |= 1 << order[j]
                p = (tuple(d), mask)
                # 再次遇到完全一样的 p，说明我们找到了一个平衡子串，左端点为 pos[p]+1，右端点为 i
                if p in pos:
                    ans = max(ans, i - pos[p])

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/longest-balanced-substring-i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。