
# 编码前缀和

前缀和的时候前缀如果有多个条件，需要用while的方式做滑动窗口处理多条件，不能直接加入

```python
while i-k>=left and c2[a] + int(s[left]==a) +1<=c[a] and c2[b]+1+ int(s[left] ==b) <=c[b] :
    c2[s[left]] +=1
    tick2 = c2[a]%2 *2  +c2[b]%2
    ls[tick2] = max(ls[tick2], -c2[a] +c2[b])
    left +=1
```