

# 问题
https://leetcode.cn/problems/minimum-partition-score/description/
https://www.bilibili.com/video/BV1mA6tBxEVC/?spm_id_from=333.1387.homepage.video_card.click&vd_source=ca787d3785cbd6247961eba27850fa0c

fi = fj + Si*Sj (0<=j<i) 
的最大最小值问题

[斜率优化实现](斜率优化.py)
[斜率优化更清晰版本](斜率优化.v2.py)

q ：记录了当前所有的candidate， q[0]维护了当前点的最优值，如果q[0]的值被pop则在后续选点中就不可能是最优值

同时q的队列也要把凹点去除,否则得到的最佳点就错误
```python
while len(q) > 1 and (q[-1] - q[-2]).det(v - q[-1]) <= 0:
        q.pop()
    q.append(v)
```

f[i] 表示 i个点分k段的时候的最小值，然后在循环中用当前循环的点作为最后一个分割点找到k+1段分割的candidate

