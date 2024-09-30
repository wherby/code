

## 枚举右，维护左
https://leetcode.cn/problems/maximize-win-from-two-segments/description/?envType=daily-question&envId=2024-09-11
https://leetcode.cn/problems/maximize-win-from-two-segments/solutions/2093246/tong-xiang-shuang-zhi-zhen-ji-lu-di-yi-t-5hlh/?envType=daily-question&envId=2024-09-11

在 X轴 上有一些奖品。给你一个整数数组 prizePositions ，它按照 非递减 顺序排列，其中 prizePositions[i] 是第 i 件奖品的位置。数轴上一个位置可能会有多件奖品。再给你一个整数 k 。

你可以选择两个端点为整数的线段。每个线段的长度都必须是 k 。你可以获得位置在任一线段上的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。


选取两个区间的最大值，如果用贪心则会错，需要维护一个区间最大值和当前点最大值计算


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        mx = 0 
        l =0
        ls = list(prizePositions)
        pre = [0]*(len(ls)+2)
        for i,a in enumerate(ls):
            while ls[i]>ls[l]+k:
                l +=1
            pre[i] = max(pre[i-1],i-l+1)
            mx = max(mx,i-l+1 + pre[l-1] )
            #print(mx,pre,i,l)
        return mx
        
