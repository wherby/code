组合问题

##
已知N个递增数组的最后一个数字为M 的组合 就为 Sum([C（i）／（i＋ｎ） for i in range(m)])
https://leetcode.com/problems/count-the-number-of-ideal-arrays/discuss/2261280/Python-Arranging-primes-intro-to-combinatorics


## “n个球放到m个盒子”问题整理(Twelvefold way) 

https://www.cnblogs.com/RioTian/p/15188528.html

### n 个球放进m个不同的盒子里 《=第二类斯特林数
algorithm/mathA/第2类斯特林数
``` python
mod = 10**9+7
MX =1001
s = [[0]*MX for _ in range(MX)]
s[0][0] =1 

for i in range(1,MX):
    for j in range(1,MX):
        s[i][j] = (s[i-1][j-1] + j * s[i-1][j]) % mod 

```
s[i][j]表示第i个人的时候有j个箱子的数量(默认箱子是一样的)，如果箱子是不一样的，还需要乘上箱子的排练数 j!


## Comb
如果mod数字是质数，则正常计算，如果是合数，就用algorithm/mathA/combination/combinationMod10 拆合数因子，或者Lucas定理
阶乘预处理，
C(n,k) = n! /(k!)*(n-k)!  


## 重复限制可以通过分析发现这个限制没有作用
https://codeforces.com/problemset/problem/1277/D
https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0421/solution/cf1277d.md


## 构造n*(n-1)//2内的数列和
https://codeforces.com/problemset/problem/847/C
https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0422/solution/cf847c.md

#



