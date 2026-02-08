

##
https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2026-02-07
这个问题用DP解法如下
```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp=[0]*3

        for a in s:
            ndp=[10**10]*3
            ndp[0] = dp[0] +1
            if a =="a":
                ndp[1] = min(ndp[1],dp[0],dp[1])
                ndp[2] = min(ndp[2],dp[2]+1)
            else:
                ndp[1] = min(ndp[1],dp[0]+1,dp[1]+1)
                ndp[2] = min(ndp[2],dp[0],dp[1],dp[2])
            dp = ndp 
        return min(dp)
```

但是也可以用前后缀状态分解，前缀只保留a ,后缀只保留b
```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = delete = s.count('a')
        for c in s:
            delete -= 1 if c == 'a' else -1
            if delete < ans:  # 手动计算 min 会快很多
                ans = delete
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/solutions/2149746/qian-hou-zhui-fen-jie-yi-zhang-tu-miao-d-dor2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
或者动态规划计算，f表示前面的值是aabb形式下删除字母，如果是a,则会把当前都删掉，或者把所有遇到的b都删掉，用f来记录当前字符串符合模式的最小删除数目

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        f = cnt_b = 0
        for c in s:
            if c == 'b':
                cnt_b += 1  # f 值不变
            else:
                f = min(f + 1, cnt_b)
        return f

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/solutions/2149746/qian-hou-zhui-fen-jie-yi-zhang-tu-miao-d-dor2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```