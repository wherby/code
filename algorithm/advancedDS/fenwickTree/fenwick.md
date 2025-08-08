#

https://cp-algorithms.com/data_structures/fenwick.html


# Fenwich handle "Range Update and Point Query" and "Range Updates and Range Queries" 
https://cp-algorithms.com/data_structures/fenwick.html


# 使用fenwickTree求解前k个物品的最小和
用两个 fenwicktree,一个保存物品个数，另一个保存物品价格，用价格作为x轴，从个数找到价格最高的第k个物品的价格，然后用到这个价格的所有物品的总价值减去次价格的超出k个的价值。。。

```Python
p = fen_cnt.bisect_min_larger(k)
if p < M: ans += fen_tot.sum(p) - (fen_cnt.sum(p) - k) * p
else: ans += fen_tot.sum(M - 1)
···

[使用fenwickTree求解前k个物品的最小和](../../codeforce/技巧/利用FenwickTree来求k个物品的最小和.py)