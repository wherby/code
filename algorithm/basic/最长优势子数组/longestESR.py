# https://leetcode.cn/contest/hhrc2022/ranking/1/
# 
# https://leetcode.cn/contest/hhrc2022/problems/0Wx4Pc/
# 用dict 记录第一次出现的值的index，再次出现则是最长优势子数组
#题目-02. 销售出色区间
#给你一份销售数量表 sales，上面记录着某一位销售员每天成功推销的产品数目。
#我们认为当销售员同一天推销的产品数目大于 8 个的时候，那么这一天就是「成功销售的一天」。
#所谓「销售出色区间」，意味在这段时间内，「成功销售的天数」是严格 大于「未成功销售的天数」。
#请你返回「销售出色区间」的最大长度。
#示例 1：
#输入：sales = [10,2,1,4,3,9,6,9,9]
#输出：5
#解释：最大销售出色区间是 [3,9,6,9,9]。
#示例 2：
#输入：sales = [5,6,7]
#输出：0

class Solution(object):
    def longestESR(self, sales):
        pre=dict({0:-1})
        res =cursum =0
        
        for i,h in enumerate(sales):
            cursum +=1 if h >8 else -1
            if cursum >0:
                res = i+1
            if cursum -1  in pre:
                res = max(res,i-pre[cursum-1])
            pre.setdefault(cursum,i)
            #print(pre)
        return res
        
        

re =Solution().longestESR([11,2,4,14,2,15,7,10,1,16,9,0,2,8,4,14,6,12,2,8,6,4,14,13,7,16,14,2,3,2,8,3,12,3,3,9,14,1,5,3,12,0,15,5,0,2,3,16,7,2,1,1,4,9,0,11,9,16,15,7,0,5,6,4,12,1,1,2,13,8,3,9,12,9,3,11,4,14,7,5,16,0,11,8,8,14,1,5,0,6,5,8,10,15,9,14,16,11,1,13])
print(re)