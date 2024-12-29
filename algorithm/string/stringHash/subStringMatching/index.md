

# Sub string matching
https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917929/ac-zi-dong-ji-pythonjavacgo-by-endlessch-hcqk/

正向匹配用string hash， 问题变成造桥问题 algorithm/string/stringHash/subStringMatching/q3291.2py

``` python
        cur_r =0
        nxt_r = 0
        for i in range(n):
            l,r = 0, n-i
            
            while l<r:
                mid = (l+r+1)>>1
                if hs.query(i,i+mid) not in dic[mid]:
                    r = mid -1
                else:
                    l=mid 
            nxt_r = max(nxt_r,i+l)
            if i == cur_r:
                if i == nxt_r:
                    return -1
                cur_r = nxt_r
                cnt +=1
```

反向匹配用Z函数，反向查找最大匹配片段：

z函数返回值表示的是从当前位置与起始位置的最大匹配，如果是字符串求当前位置为结尾的最大匹配，则需要把最大匹配对应累记到末尾位置，并且累积数组需要前推最大值
algorithm/string/zfunction/z函数使用.py

```python 
            for i,a in enumerate(zst):
                rls[i+a-1] = max(rls[i+a-1],a)
        for i in range(n-2,-1,-1):
            rls[i] = max(rls[i], rls[i+1] -1)
```