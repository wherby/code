# 反向计算
# 如果 i>=k时， f[i] =1 表示得到的分数是1 
# 如果 i<k 的时候， f[i] 则是由这个点可以得到的分数计算而来 然后除以长度，则变为了概率
# 这里把 得分反向求概率， 而dfs方法的时候，也是用同样的方法

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        f = [0.0] * (n + 1)
        s = 0.0
        for i in range(n, -1, -1):
            f[i] = 1.0 if i >= k else s / maxPts
            # 当前循环计算的是 f[i+1] + ... + f[i+maxPts]
            # 下个循环计算的是 f[i] + ... + f[i+maxPts-1]，多了 f[i]，少了 f[i+maxPts]
            s += f[i]
            print(s)
            if i + maxPts <= n:
                s -= f[i + maxPts]
            print(s,f)
        return f[0]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/new-21-game/solutions/3755107/hua-dong-chuang-kou-you-hua-dpjian-ji-xi-lybl/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

print(Solution().new21Game(6,1,10))