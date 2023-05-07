# https://leetcode.cn/problems/1GxJYY/
# 力扣嘉年华的花店中从左至右摆放了一排鲜花，记录于整型一维矩阵 flowers 中每个数字表示该位置所种鲜花的品种编号。你可以选择一段区间的鲜花做成插花，且不能丢弃。
# 在你选择的插花中，如果每一品种的鲜花数量都不超过 cnt 朵，那么我们认为这束插花是 「美观的」。

# 例如：[5,5,5,6,6] 中品种为 5 的花有 3 朵， 品种为 6 的花有 2 朵，每一品种 的数量均不超过 3
# 请返回在这一排鲜花中，共有多少种可选择的区间，使得插花是「美观的」。

class Solution:
    def beautifulBouquet(self, fs: List[int], cnt: int) -> int:
        n = len(fs)
        left = 0 
        sm = [0]*(n)
        dic =defaultdict(int)
        for i,a in enumerate(fs):
            dic[a] +=1
            while dic[a]> cnt:
                sm[left] = i-left
                dic[fs[left]] -=1
                left +=1
        for i in range(left,n):
            sm[i] = n-i 
        mod = 10**9+7 
        return sum(sm)%mod