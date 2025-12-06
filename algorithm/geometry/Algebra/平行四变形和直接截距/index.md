# 平行四边形特性
 平行四边形对角线上的中点重合

# 求梯形数量
转换为所有方向上斜率相等的不同截距的组合乘积和，减去平行四边形的数量


https://leetcode.cn/problems/count-number-of-trapezoids-ii/solutions/3728529/tong-ji-zhi-xian-qu-diao-zhong-fu-tong-j-a3f9/?envType=daily-question&envId=2025-12-03

关于思考题：

正方形：枚举对角线AC，即可确定中点O，AC绕O旋转90度即可确定BD。
菱形：枚举对角线AC，即可确定直线AC与中点O，另一条对角线BD需要满足AC⊥BD、且中点与O重合。
矩形：枚举对角线AC，即可确定中点O，另一条对角线BD需要满足∣AC∣=∣BD∣、且中点与O重合。
等腰梯形：枚举一条底边AB，即可确定中点E，另一条底边CD需要满足CD∥AB且不共线，且CD中点F满足EF⊥AB。（存疑：平行四边形算不算等腰梯形？）
直角梯形：枚举一条底边AB，另一条底边CD需要满足CD∥AB且不共线，不妨令其中一个顶点C满足AC⊥AB，则另一个顶点D满足D相对于C与B相对于A同侧。
以上判断垂直、方向可以使用向量运算、计算点在直线上的投影解决。