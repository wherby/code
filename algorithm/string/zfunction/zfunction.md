# 
https://www.youtube.com/watch?v=CpZh4eF8QBw&ab_channel=TusharRoy-CodingMadeSimple
https://cp-algorithms.com/string/z-function.html



## Z 函数

求当前子串与prefix匹配的数量

https://leetcode.cn/contest/weekly-contest-415/problems/minimum-number-of-valid-strings-to-form-target-ii/description/


## questions

https://leetcode.cn/contest/weekly-contest-415/problems/minimum-number-of-valid-strings-to-form-target-ii/submissions/564938556/


## Z 函数使用
z函数返回值表示的是从当前位置与起始位置的最大匹配，如果是字符串求当前位置为结尾的最大匹配，则需要把最大匹配对应累记到末尾位置，并且累积数组需要前推最大值

```python 
            for i,a in enumerate(zst):
                rls[i+a-1] = max(rls[i+a-1],a)
        for i in range(n-2,-1,-1):
            rls[i] = max(rls[i], rls[i+1] -1)
```