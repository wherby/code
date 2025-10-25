
# 由后到前，贪心寻找前m位，增加最低位数字， 判断新的m位数字可以由已经存在m位前序字母组成，
# 然后记录m位中的剩余字母，再在剩余位数上做0/1背包求取最小组合，再把m位后面的数字组成最小数字

from typing import List, Tuple, Optional

class Solution:
    # 从 a 中选一个字典序最小的、元素和等于 target 的子序列
    # a 已经从小到大排序
    # 无解返回 None
    def zeroOneKnapsack(self, a: List[int], target: int) -> Optional[List[int]]:
        n = len(a)
        f = [False] * (target + 1)
        f[0] = True
        from_ = [[0] * (target + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            v = a[i]
            for j in range(target, v - 1, -1):
                if f[j - v]:
                    f[j] = True
                    from_[i][j] = j - v  # 记录转移来源

        if not f[target]:
            return None

        ans = []
        i, j = 0, target
        while j > 0:
            ans.append(j - from_[i][j])
            j = from_[i][j]
            i += 1
        return ans

    def nextBeautifulNumber(self, n: int) -> int:
        s = "0" + str(n)  # 补一个前导零，方便处理答案十进制比 n 的十进制长的情况
        s = list(map(int, s))  # 避免在后续循环中反复调用 int
        m = len(s)

        MX = 10
        cnt = [0] * MX
        for i in range(1, m):
            cnt[s[i]] += 1

        # 从右往左尝试
        for i in range(m - 1, -1, -1):
            if i > 0:
                cnt[s[i]] -= 1  # 撤销

            # 增大 s[i] 为 j
            for j in range(s[i] + 1, MX):
                cnt[j] += 1

                # 后面 [i+1, m-1] 需要补满 0 < cnt[k] < k 的数字 k，剩余数位可以随便填
                free = m - 1 - i  # 统计可以随便填的数位个数
                for k, c in enumerate(cnt):
                    if k < c:  # 不合法
                        free = -1
                        break
                    if c > 0:
                        free -= k - c
                if free < 0:  # 不合法，继续枚举
                    cnt[j] -= 1
                    print(cnt,j,i)
                    continue

                # 对于可以随便填的数位，计算字典序最小的填法
                a = [k for k in range(1, MX) if cnt[k] == 0]
                missing = self.zeroOneKnapsack(a, free)
                if missing is None:  # 无解，继续枚举
                    cnt[j] -= 1
                    continue

                for v in missing:
                    cnt[v] = -v  # 用负数表示可以随便填的数

                s[i] = j
                del s[i + 1:]
                for k, c in enumerate(cnt):
                    if c > 0:
                        c = k - c
                    elif c < 0:
                        c = -c
                    s += [k] * c
                return int(''.join(map(str, s)))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/next-greater-numerically-balanced-number/solutions/3814255/liang-chong-fang-fa-mei-ju-dao-xu-tan-xi-164n/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# re = Solution().nextBeautifulNumber(111111112222232333333444455555666666)
# print(re)
# re = Solution().nextBeautifulNumber(999999999999999999999)
# print(re)
# re = Solution().nextBeautifulNumber(111111111111111111111)
# print(re)
re = Solution().nextBeautifulNumber(999999999)
print(re)