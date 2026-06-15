

# WQS 二分 (AlienDP) 
题目：
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/

https://leetcode.cn/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/description/


# WQS 二分实现
[二分的实质](WQS二分的实质.md)
```
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/
给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
```
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/536396/yi-chong-ji-yu-wqs-er-fen-de-you-xiu-zuo-x36r/

对于次数在K次以内的交易，理论上每多一次交易，其收益的边界效益会减少
在交易过程中，对每次交易施加一个成本， 求取在当前成本上能交易的最多交易次数。如果收益相同，则多次交易取胜。
在有交易成本的条件下，二分，其实是用成本匹配了交易的收益率，只有大于等于当前成本的交易可以成立，这样求交易次数是线性的。


# AlienDP 模版

[AlienDP模版](AlienDP模版.py)
[直接变成有有代价的二分模版，更简单](wqs二分的另一种写法.py)