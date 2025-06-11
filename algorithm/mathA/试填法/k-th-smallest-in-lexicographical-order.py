# https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/description/?envType=daily-question&envId=2025-06-09
# 计算首位开始的所有数字试填
# https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/solutions/3696254/zai-shi-cha-shu-shang-zhao-di-k-xiao-olo-vzkl/?envType=daily-question&envId=2025-06-09
# 也可以考虑成对树上节点的访问
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def getStep(cur):
            step,first,last = 0,cur,cur 
            while first <= n :
                step +=min(last,n) - first +1 
                first *=10
                last =last*10 +9 
            return step 
        k -=1
        cur = 1 
        while k:
            step = getStep(cur)
            if step <=k:
                k -= step
                cur +=1
            else:
                cur *=10
                k -=1
        return cur 

re = Solution().findKthNumber(10,3)
print(re)