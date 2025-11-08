# 因为可以知道数字的上界是多少位，所以可以用填前导零的方式确定搜索位数
# 在填数字之后，往后搜索是否当前的选择能成功，如果成功则填入，否则不填
# t // gcd(t, d) 保证了t能被消去，如剩下2，填的数字是4 的时候
from functools import cache

from math import gcd

class Solution:
    def smallestNumber(self, s: str, t: int) -> str:
        tmp = t
        cnt = 0
        for p in 2, 3, 5, 7:
            while tmp % p == 0:
                tmp //= p
                cnt += 1
        if tmp > 1:  # t 包含其他质因子
            return "-1"

        # 补前导零（至少一个）
        cnt = max(cnt - len(s) + 1, 1)
        s = '0' * cnt + s

        n = len(s)
        ans = ['0'] * n

        @cache  # 仅仅作为 vis 标记使用
        def dfs(i: int, t: int, is_limit: bool) -> bool:
            if i == n:
                return t == 1

            if is_limit and i < cnt and dfs(i + 1, t, True):  # 填 0（跳过）
                return True

            low = int(s[i]) if is_limit else 0
            for d in range(max(low, 1), 10):
                if dfs(i + 1, t // gcd(t, d), is_limit and d == low):
                    ans[i] = str(d)
                    return True
            return False

        dfs(0, t, True)
        dfs.cache_clear()  # 防止爆内存
        return ''.join(ans).lstrip('0')  # 去掉前导零

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/smallest-divisible-digit-product-ii/solutions/2984014/bao-sou-zuo-fa-lei-si-shu-wei-dp-by-endl-nkoo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。