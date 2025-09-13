

# [GCD 容斥原理](https://leetcode.cn/problems/sorted-gcd-pair-queries/)
子数组的GCD 为a,则所有数字都能被a整除
所有数字都能被a整除，则子数组GCD为 Na, 要求出为a的子数组数目，则要减去大于a 的子数组数目[复数因子](容斥原理 algorithm/mathA/gcd/倍数容斥gcd.py)
[直接计算容斥数字](莫比乌斯gcd.py)


# [递增子序列GCD](# https://leetcode.cn/problems/sum-of-beautiful-subsequences/description/)
由于有GCD除数因子，所以可以用遍历GCD 除数因子的方式获取所有可能的排列
递增序列数量是可以由FenwickTree DP方式求取， 之后利用容斥原理，去除复数因子
由于求每个GCD因子都需要重置FenwickTree,为了减少重置时间，使用timestamp作为懒初始化标志 [懒初始化](递增子序列gcd.py)
因为是求每个GCD因子a，所以每次FenwickTree初始化可以不使用n长度，而使用n//a 长度，因为子序列都能被 a 整除，所以可以压缩数轴 使得 n**2 规模变成 nlogn [压缩值域空间](递增子序列gcd.2.py) 反而比懒初始化的算法快
GCD 的本质是把数组从单位元空间 映射 到另一个空间作filter 


# [莫比乌斯函数](../组合数学/计算互质的对数/coPrimeWithMoAlgo.py)
[利用莫比乌斯函数计算互质](../组合数学/计算互质的对数)

# [数论解决利用偶拉函数](利用数论.py)