#

https://leetcode.com/contest/weekly-contest-469/problems/number-of-zigzag-arrays-ii/description/

使用矩阵运算的时候，由于各个点有不同的方向，A状态运算矩阵之后变成B状态，这时候就不能继续使用相同矩阵

## 原始问题
按照一般的做法，元素问题有M个点，每个点都有两个运动方向，所以把矩阵扩展到2*M阶矩阵，然后做矩阵乘法，这时由于矩阵扩展2倍，导致矩阵运算增加8倍运算量
[使用矩阵扩展解决方向问题](qickerVersion.py)

## 矩阵压缩
因为有两个不同的方向会导致矩阵2倍规模扩展，如果经过两次运算，这时候方向一致，这就不用2倍扩展
[双倍运算使得方向一致](smallmatrix.py)
在双倍扩展的时候，如果多出来一次，则把后一个矩阵再放前面运算一次矩阵乘法

## 使用对称性
使用对称性，在转移的时候，把对称方向转向，这样每次矩阵运算都是同方向的运动了
https://leetcode.cn/problems/number-of-zigzag-arrays-ii/solutions/3794101/ju-zhen-kuai-su-mi-you-hua-dppythonnumpy-77e7/
[使用对称性，在转移的同时翻转转移对象的方向](test.py)
以M= 5， i=0为例， 这时候向上转移， 0可以达到 [0,1,1,1,1] 的地方，但是下一次是向下转移，则把向量翻转成[1,1,1,1,0]，变成了向上转移,从此每次运算都是同方向

