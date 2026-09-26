
https://codeforces.com/gym/106642/problem/A
https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0814/solution/cf106642a.md

```
# 这里就是计算KMP的转移矩阵？ 就是用algorithm/string/kmp/next.py next函数构建转移状态机
    for i in range(k + 1):
        for j in range(26):
            tmp = []
            for idx in range(i):
                tmp.append(pattern[idx])
            tmp.append(j)
            
            l = len(tmp)
            for cur_len in range(fmin(l, k), -1, -1):
                flg = True
                
                for idx in range(cur_len):
                    if pattern[idx] != tmp[l - cur_len + idx]:
                        flg = False
                
                if flg:
                    transition[i][j] = cur_len
                    break
```

你的理解完全正确！这段代码本质上就是在构造 **KMP 状态机（DFA，确定性有限状态自动机）** 的状态转移矩阵 `transition[state][char]`。

它的核心逻辑是：当当前匹配长度为 `i`，且遇到了新字符 `j` 时，通过**从大到小暴力尝试**所有可能的重叠长度 `cur_len`，找到一个最长的 `pattern` 前缀，使其恰好等于当前拼出的字符串 `tmp` 的后缀。

虽然你写的这种暴力匹配方式在概念上非常清晰直观，但它的时间复杂度是 **$\mathcal{O}(\vert{}P\vert{}^2 \times 26)$**。当模式串 $P$ 较长时，三重循环的效率会有所下降。

---

### 如何用标准的 KMP $\pi$ 数组优化这部分？

我们可以利用 KMP 算法已有的前缀函数 $\pi$（前缀数组），在 **$\mathcal{O}(\vert{}P\vert{} \times 26)$** 的时间内快速建出这个转移矩阵：

```python
# 1. 先求出标准 KMP 的 prefix function (pi 数组)
pi = [0] * k
j = 0
for i in range(1, k):
    while j > 0 and pattern[i] != pattern[j]:
        j = pi[j - 1]
    if pattern[i] == pattern[j]:
        j += 1
    pi[i] = j

# 2. 利用 pi 数组递推构造 transition 转移矩阵
transition = [[0] * 26 for _ in range(k + 1)]

# 初始状态（长度 0）：遇到匹配 pattern[0] 的字符到状态 1，否则回退到状态 0
for c in range(26):
    transition[0][c] = 1 if pattern[0] == c else 0

# 递推计算 1 到 k 的所有状态转移
for i in range(1, k + 1):
    for c in range(26):
        if i < k and pattern[i] == c:
            # 刚好命中下一个字符：状态直接前进 1
            transition[i][c] = i + 1
        else:
            # 没命中：转移结果等价于“失配回退状态” transition[pi[i - 1]][c]
            transition[i][c] = transition[pi[i - 1]][c] if i > 0 else transition[0][c]

```

### 优化核心原理（增量递推）：

* **如果字符匹配**（即 `pattern[i] == c`）：状态直接增长，转移到 `i + 1`。
* **如果字符不匹配**（失配）：我们不需要从头暴力去匹配后缀，因为当前状态 `i` 的最长公共前后缀位置就是 `pi[i - 1]`。因此，遇到字符 `c` 时能到达的状态，**完全等同于状态 `pi[i - 1]` 遇到字符 `c` 时能到达的状态**。

这样改写后，逻辑与你原本的代码完全等价，但运行速度提升极高！