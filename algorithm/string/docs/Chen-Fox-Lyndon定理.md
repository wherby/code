
https://codeforces.com/gym/106598/problem/M

https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0908/solution/cf106598m.md
字典序传递性

这里涉及的结论推导和 **Chen–Fox–Lyndon 定理**（陈-福克斯-林登定理）是组合字符串理论（Combinatorics on Words）中非常经典的知识。

---

### 一、 “$s^p t^q$ 与 $t^q s^p$ 的比较等价于 $s+t$ 与 $t+s$” 的推导过程

这个结论本质上是关于**无限重复串**与**有限前缀比较**的关系。

#### 1. 寻找第一个不同字符（Mismatch）

字典序比较的核心规则是：**两个字符串的大小由它们“第一个不相同的字符”决定**。

考虑字符串 $A = s^p t^q$ 和 $B = t^q s^p$：

* $A$ 是由 $p$ 个 $s$ 后面接 $q$ 个 $t$ 组成的。在前 $\vert{}s\vert{} \times p$ 个字符中，它完全是 $s$ 的重复。
* $B$ 是由 $q$ 个 $t$ 后面接 $p$ 个 $s$ 组成的。在前 $\vert{}t\vert{} \times q$ 个字符中，它完全是 $t$ 的重复。

#### 2. 无限串 $s^\infty$ 与 $t^\infty$ 的比较

假设我们把 $s$ 和 $t$ 无限重复拼接下去，得到两个无限长的字符串 $s^\infty$ 和 $t^\infty$。
如果 $s^\infty \neq t^\infty$，它们必然会在某一个有限的位置 $i$ 出现首次不同：


$$s^\infty[i] \neq t^\infty[i]$$

这个首次出现差异的位置 $i$ 会有多远呢？
根据周期字符串的性质（Periodicity Lemma），如果 $s^\infty$ 和 $t^\infty$ 在长度为 $\vert{}s\vert{} + \vert{}t\vert{}$ 的前缀内完全相同，那么它们必然全局完全相同（即 $s$ 和 $t$ 共享同一个最小基本循环节，$s+t = t+s$）。

因此：

* **如果 $s^\infty \neq t^\infty$**：第一个不同字符的位置 $i$ **必然出现**在 $s^\infty$ 和 $t^\infty$ 的前 $\vert{}s\vert{} + \vert{}t\vert{}$ 个字符以内。
* 而对于 $s+t$ 与 $t+s$，它们的总长度恰好就是 $\vert{}s\vert{} + \vert{}t\vert{}$！
* 这意味着：$s^\infty$ 与 $t^\infty$ 在位置 $i$ 的差异，**完全等价**于 $s+t$ 与 $t+s$ 在位置 $i$ 的差异。

#### 3. 为什么 $s^p t^q$ 也能套用这个结论？

只要 $p \ge 1$ 且 $q \ge 1$：

* $s^p t^q$ 的前 $\vert{}s\vert{} + \vert{}t\vert{}$ 个字符与 $s^\infty$ 的前 $\vert{}s\vert{} + \vert{}t\vert{}$ 个字符完全相同（因为 $\vert{}s\vert{} \cdot p + \vert{}t\vert{} \cdot q \ge \vert{}s\vert{} + \vert{}t\vert{}$）。
* $t^q s^p$ 的前 $\vert{}s\vert{} + \vert{}t\vert{}$ 个字符与 $t^\infty$ 的前 $\vert{}s\vert{} + \vert{}t\vert{}$ 个字符完全相同。

所以，决定 $s^p t^q$ 与 $t^q s^p$ 大小关系的那个“关键差异位置”，必定落在了 $s+t$ 与 $t+s$ 的比较范围内。

* 若 $s+t < t+s$ $\implies$ $s^\infty < t^\infty$ $\implies$ $s^p t^q < t^q s^p$
* 若 $s+t > t+s$ $\implies$ $s^\infty > t^\infty$ $\implies$ $s^p t^q > t^q s^p$
* 若 $s+t = t+s$ $\implies$ $s$ 和 $t$ 可交换 $\implies$ $s^p t^q = t^q s^p$

---

### 二、 什么是 Chen–Fox–Lyndon 定理？

**Chen–Fox–Lyndon 定理**（通常简称为 **Lyndon 分解定理**）由 Kuo-Tsai Chen（陈国才）、Ralph Fox 和 Roger Lyndon 于 1958 年提出。它是组合字符串和自由李代数（Free Lie Algebra）中的一个基础定理。

在理解定理前，需要先了解 **Lyndon 词（Lyndon Word）** 的定义。

#### 1. 什么是 Lyndon 词？

一个非空字符串 $w$ 如果满足：**它在字典序上严格小于它的所有非平凡循环后缀（或后缀）**，那么 $w$ 就被称为 Lyndon 词。
简单来说，Lyndon 词是它自身所有循环移位串中**字典序唯一最小**的那个串（且不能由更短的串周期重复组成）。

[Duval.py](Duval.py)

* **示例（假设字符集 $\{a, b\}$，且 $a < b$）：**
* `a`, `b` 是 Lyndon 词。
* `ab` 是 Lyndon 词（其后缀只有 `b`，`ab < b`）。
* `aab`, `abb`, `aabab` 都是 Lyndon 词。
* `aba` **不是** Lyndon 词（因为后缀 `a < aba`）。
* `abab` **不是** Lyndon 词（因为它有周期，且不是严格小于后缀）。



#### 2. 定理内容

**Chen–Fox–Lyndon 定理：**

> 任意一个非空字符串 $w$，都可以**唯一地**表示为若干个 Lyndon 词的拼接：
> 
> $$w = w_1 w_2 \dots w_k$$
> 
> 
> 
> 使得这些 Lyndon 词满足**字典序单调不增**的顺序：
> 
> $$w_1 \ge w_2 \ge \dots \ge w_k$$
> 
> 

* **示例：**
* 字符串 $w = \text{"bbaaba"}$
* 唯一分解为：$\text{"b"} \cdot \text{"b"} \cdot \text{"aaba"}$
* 其中 $\text{"b"} \ge \text{"b"} > \text{"aaba"}$，每个因子都是 Lyndon 词。



#### 3. 这个定理与本题的关系

虽然解决本题不需要直接运行 Duval 算法（求解 Lyndon 分解的线性时间算法），但 Lyndon 词的相关定理给出了字符串可交换性（Commutativity）的重要推论：

1. **可交换定理（Defining Commutativity）：**
对于两个非空串 $s$ 和 $t$，$st = ts$ 当且仅当 $s$ 和 $t$ 具有相同的基本 Lyndon 周期（即 $s = r^a, t = r^b$）。
2. **字典序传递性（Lexicographical Monotonicity）：**
在 Lyndon 理论中，如果 $st < ts$，则对任意 $p, q \ge 1$，都有 $s^p t^q < t^q s^p$。

这就为提示中的“无限周期串比较可简化为 $s+t$ 与 $t+s$ 的比较”提供了严密的数学代数支撑。