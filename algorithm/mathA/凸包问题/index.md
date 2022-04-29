
# Question
https://leetcode-cn.com/problems/erect-the-fence/

## method 1 
解题思路 本题为凸包问题，采用通用的思路求解，对点进行x和y轴大小排序，判断最近三点的形成的边与点的位置关系，如何才能满足包含最近的其他点，
要分开讨论本题分为上凸包和下凸包两个不同情况，分别从左边的点开始和从最右边的点开始判断当前点在前面两个点连线的左边还是右边，在右边能获得更大的凸包。
./code/method1.py



##
https://leetcode-cn.com/problems/erect-the-fence/solution/an-zhuang-zha-lan-by-leetcode-solution-75s3/
