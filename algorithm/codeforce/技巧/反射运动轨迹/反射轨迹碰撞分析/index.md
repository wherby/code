

## 运动轨迹分析 [运动轨迹分析](pay_off_satwik_sinha_source_code.cpp)
 https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/E?source=facebook
题目中两个物体在L的区域往复运动，假设A物体在A的初始位置，B物体在B的初始位置，开始往左运动，则第一次碰撞的时间为(A+B)/2， 第2次碰撞的时间是什么呢？
观察得到碰撞的点应该是基于L中心对称，则 下一次在 L + （A+B)/2 的时间上会碰撞

如果T时间内最后一次碰撞， Tres = T %L
则 (A+B)/2 <Tres
或者 （A+B/2)<Tres+L if T > Tres


(A+B)/2 <Tres 内有值，则取这个值
如果
 (A+B)/2 <Tres 内没有值， 且 T > Tres, 则最后一次碰撞在Tres+L处前的最大值就是在L中B的最大值

