

## 带权子数组和

1*第一个子数组和 + 2*第2个子数组和 + ，，+N * 第N个子数组和 = 后缀数组和

algorithm/dp/OTDP/dividArray/OTversion.py  这里实现的是3阶 L,R,i， 用上面的方法把i消去

## 使用系统自带max timeout,需要自己定义函数
max = lambda a, b: b if b > a else a
https://leetcode.cn/problems/maximum-profit-from-trading-stocks-with-discounts/submissions/632329149/