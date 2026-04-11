# https://leetcode.cn/problems/count-the-number-of-substrings-with-dominant-ones/submissions/678247014/?envType=daily-question&envId=2025-11-15
# 平方根优化，用开始点确定块是否能有贡献，同时用约束条件计算有效块的结束位置

# 给你一个二进制字符串 s。
# 请你统计并返回其中 1 显著 的 子字符串 的数量。
# 如果字符串中 1 的数量 大于或等于 0 的数量的 平方，则认为该字符串是一个 1 显著 的字符串 。

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        zels =[-1]
        cnt = 0 
        for i,a in enumerate(s):
            if a == "0":
                zels.append(i)
            if len(zels) > 202:
                zels= zels[-201:]
            c0 = 0
            toidx = i 
            for a in zels[::-1]:
                if i-a-c0 >=c0**2:
                    rightIdx = min(toidx,i+1- c0-c0**2)
                    cnt += rightIdx-a
                c0 +=1
                toidx = a
        return cnt

re =Solution().numberOfSubstrings("00011")
print(re)