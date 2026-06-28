
# 
https://leetcode.cn/problems/number-of-zigzag-arrays-ii/description/?envType=daily-question&envId=2026-06-24
给你三个整数 n、l 和 r。

长度为 n 的锯齿形数组定义如下：

每个元素的取值范围为 [l, r]。
任意 两个 相邻的元素都不相等。
任意 三个 连续的元素不能构成一个 严格递增 或 严格递减 的序列。
返回满足条件的锯齿形数组的总数。

由于答案可能很大，请将结果对 109 + 7 取余数。

序列 被称为 严格递增 需要满足：当且仅当每个元素都严格大于它的前一个元素（如果存在）。

序列 被称为 严格递减 需要满足，当且仅当每个元素都严格小于它的前一个元素（如果存在）。


## 如何建立矩阵
这个题目可以利用对称性，得到起点相同，方向不同的所有起始状态，在方向不同的时候的变换矩阵是相反的
如果直接建立 d =r-l+1 大小的矩阵，则会有奇偶性的问题，因为在每次变换之后，会交换当前运动的方向，这时如果直接快速幂2倍的话，就需要考虑(n-1)的奇偶性，还要补余数1
arr1 = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
arr2 = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]

https://leetcode.cn/problems/number-of-zigzag-arrays-ii/solutions/3794101/ju-zhen-kuai-su-mi-you-hua-dppythonnumpy-77e7/?envType=daily-question&envId=2026-06-24
这时，把方向状态编码到位置上，这样的转移矩阵就变成一维的矩阵
arr3 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

但是这样就会增加4倍的矩阵计算时间，这时我们把矩阵的定义的index从新定义，认为矩阵的行表示INDEX为 0, 1,2,3，..d-1 ,矩阵的列表示 d-1, d-2,..0, 这时就会发现状态转移和方向是没有关系的了，两种状态转移的矩阵是同一个矩阵
arr4 = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]

```python
d = 3
arr1 = [[0]*d for _ in range(d)]
for i in range(d):
    for j in range(i+1,d):
        arr1[i][j] = 1 
print(arr1)
arr2 = [[0]*d for _ in range(d)]
for i in range(d):
    for j in range(i):
        arr2[i][j] = 1 
print(arr2)

arr3 = [[0]*2*d for _ in range(2*d)]
for i in range(d):
    for j in range(i):
        arr3[i][d+j] = 1
    for j in range(i+1,d):
        arr3[d+i][j] =1
print(arr3)
arr4 = [[0]*d for _ in range(d)]
for i in range(d):
    for j in range(d-1-i):
        arr4[i][j] = 1 
print(arr4)
```

## 算法优化：
Berlekamp-Massey 算法 + Kitamasa 算法 ：https://leetcode.cn/problems/number-of-zigzag-arrays-ii/solutions/3794101/ju-zhen-kuai-su-mi-you-hua-dppythonnumpy-77e7/?envType=daily-question&envId=2026-06-24
