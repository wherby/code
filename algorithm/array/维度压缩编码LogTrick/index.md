
## 动态维度压缩LogTrick
https://leetcode.cn/problems/longest-balanced-substring-i/
一个字母序列固定左端点，查找右端点的时候，可能形成的mask 有 2**26 种可能，但是一个已知的序列，如果从右往左看，找到左端点右边第一个出现的字符，则在任意固定左端点而言，最多只有26种可能的mask
```python
suf_orders = [None] * n
order = []
for i in range(n - 1, -1, -1):
    # 把最近出现的字母移到 order 末尾
    try: order.remove(s[i])
    except: pass
    order.append(s[i])
    suf_orders[i] = order[:]
```

因为有26种mask，所以匹配的时候就需要做26种mask的基准，这里选用最小字典序作为相减，其实这里选择第一个出现的字符也可以，“第一个出现的字符”指mask里第一个置位
```python
 for i, b in enumerate(s):
    suf_order = suf_orders[i]
    min_ch = inf
    mask = 0
    for j in range(len(suf_order) - 1, -1, -1):
        min_ch = min(min_ch, suf_order[j])
        # 注意此时 cnt 并不包含 s[i]，我们计算的是前缀 s[:i] 的信息
        # 在子串中的字母，计算差值
        # 不在子串中的字母，维持原样
        d = cnt[:]
        for ch in suf_order[j:]:
            d[ch] -= cnt[min_ch]
        mask |= 1 << suf_order[j]
        p = (tuple(d), mask)  # mask 用来区分 d[ch] 是差值还是原始值
        # 记录 p 首次出现的位置
        if p not in pos:
            pos[p] = i - 1
```

从左到右和从右到左，分别表示将要加入新字符序列和已经加入序列，用将要加入的序列mask提取特征值，用已经加入的序列mask恢复特征值