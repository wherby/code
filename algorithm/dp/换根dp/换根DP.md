

# 换根DP
## 路径求值,
换根影响：
求节点下子路径的最大值和次大值，并且记录最大值的子节点  https://leetcode.cn/problems/time-taken-to-mark-all-nodes/solutions/2868276/di-er-lei-huan-gen-dppythonjavacgo-by-en-411w/
如果路径是是矢量，则需要用当前路径和父节点的最大值或者次大值进行延伸DP

路径值与方向有关的矢量路径 ： 
[矢量路径](树上换根DP求矢量路径最大值.py)

## 换根影响： 只有换根路径会产生影响
[换根对整体统计的影响](../treedp/reRoot.py)