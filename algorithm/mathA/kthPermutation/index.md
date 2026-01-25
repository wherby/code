

##  Kth dp permutation 
[给你两个整数 n 和 k，一个 交替排列 是前 n 个正整数的排列，且任意相邻 两个 元素不都为奇数或都为偶数。](../../dp/kthOrderPermutation/permutations-iv.py)


## basic permutation function 

[permutation basic helper function ](kthPermutationBasic.py)

## 试填法从高到低试填，先计算最高位取

## [试填法找到第K个permutation](试填法permutation.py)
在当前位从低到高填入数字，然后计算填入数字的排列，如果排列大于K，则证明当前位置填K是可以的，否则在当前位寻找下一个数字

### [01 试填](../../dp/dpWithStatus-Number/倒序贪心寻找下一个符合条件的数字/index.md)
在当前位试填0，然后计算排列，如果大于则需要填1

## [如果数字太大kth排列值不能计算的情况怎么用多项式表达获取下K位的排列](permutaion进位技巧.py)
排列值的多项式表达，子排列的数字集不一致情况下的同余排列怎么求