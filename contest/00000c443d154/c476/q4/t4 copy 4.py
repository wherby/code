# 前缀和，记录下一段开始的左端点
from typing import List, Tuple, Optional


class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n= len(nums)
        pre = [0]*(n+1)
        cnt = 0 
        for i,x in enumerate(nums):
            if i > 0 and x < nums[i-1]:
                cnt =0 
            cnt +=1
            pre[i+1] = pre[i] + cnt 
        # nxt[i] 表示 i 右边下一个递增段的左端点，若不存在则为 n
        nxt = [0] * n
        nxt[-1] = n 
        for i in range(n-2,-1,-1):
            nxt[i] = nxt[i+1] if nums[i]<= nums[i+1] else i+1 
        
        ans = []
        for l,r in queries:
            l2 = nxt[l] 
            if l2 >r: 
                m = r-l+1
                ans.append(m*(m+1)//2)
                continue
            # l 和 r 在不同区间
            # 分成 [l, l2) + [l2, r]
            # 由于 [l2, r] 中的每个右端点对应的左端点都在 [l2, r] 内，所以可以用前缀和计算
            m = l2 - l
            ans.append(m * (m + 1) // 2 + pre[r + 1] - pre[l2])
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-stable-subarrays/solutions/3832945/fen-duan-er-fen-cha-zhao-qian-zhui-he-py-ukgs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re =Solution().countStableSubarrays(nums =[5,25,15,6], queries = [[1,3],[3,3]])
print(re)





re =Solution().countStableSubarrays(nums = [3,4,2], queries = [[1,2]])
print(re)