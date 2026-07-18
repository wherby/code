
# 等式变换题目

You are given a positive integer 𝑛. Count the number of pairs of integers (𝑎,𝑏)
 with 1≤𝑎<𝑏≤𝑛
 such that (𝑏−𝑎)
 divides 𝑎⋅𝑏.
 https://codeforces.com/gym/106619/problem/B
 https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0714/solution/cf106619b.md

a*b = b*b  -(b-a)*b 因为 a*b 整除 (b-a) 所以 b*b 整除 （b-a) 所以等价于求 b*b 中 （b-a)整除的因子数 其中  0<（b-a)<b
等价于求 b*b 的因子个数的一半？ 因为 b*b 因数分解 的因子 一定有一个是大于 b 一个小于b ,还有一个特殊值的分解是两个都等于b， 这个就用整除去掉就好了


