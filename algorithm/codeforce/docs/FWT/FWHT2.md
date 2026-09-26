https://codeforces.com/gym/102129/problem/A
https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0829/solution/cf102129a.md


```
其实每次递归调用就是求不同频率上的FFT和IFFT？
```

是的，**你的理解非常到位！**

如果把这段代码映射到 FFT / FWT 的视角，**每一次递归调用 `solve(w1, w2)`，确实就是在求解原信号在某一个特定“频域分量（或基基向量子空间）”上的点积**，而递归结束后的线性加减组合，就承担了 **IFFT（逆变换）** 的功能。

---

### **1. 递归入参 `w1, w2` $\to$ 在做正向变换（FFT/FWT）**

在 FFT 中，正变换（FFT）的作用是把时域上的信号向量通过矩阵乘法 $\hat{x} = M \cdot x$ 转换到频域。

看看代码里在调用 `solve` 前对 `w1` 和 `w2` 做的事情：

* **第一次调用**：$w_1 = v_1 + v_2$。这实际上就是在计算频域基底上的一个基向量 $\begin{pmatrix} 0 & 1 & 1 \end{pmatrix} \cdot \begin{pmatrix} v_0 \\ v_1 \\ v_2 \end{pmatrix}$。
* **第四次调用**：$w_1 = v_0 + v_1 + v_2$。这对应于 DC 分量（零频分量/全频带分量），即基向量 $\begin{pmatrix} 1 & 1 & 1 \end{pmatrix} \cdot \begin{pmatrix} v_0 \\ v_1 \\ v_2 \end{pmatrix}$。

每次在递归前把不同时域段 $v_0, v_1, v_2$ 按系数相加，**就是在将时域信号投影到某一个特定的频域基底上**。

---

### **2. 递归基 `cur_len == 1` $\to$ 频域点乘（Pointwise Multiplication）**

当递归一直向下，把每一位（每一个频域维度）都投影完成后，最终到达最底层 `cur_len == 1`：

```python
if cur_len == 1:
    return [x1[0] * x2[0]]

```

此时 `x1[0]` 和 `x2[0]` 已经是两个信号在最高维频域点上的响应值。**这里的普通标量乘法 `x1[0] * x2[0]`，正是 FFT 算法核心中的“频域逐点相乘”！**

---

### **3. 递归返回后的加减组合 $\to$ 在做逆变换（IFFT）**

在标准 FWT 中，点乘结束后需要乘上逆矩阵 $M^{-1}$ 才能把频域结果变回时域。

看看代码最后求 `ans[2 * ncur_len + i]` 时的操作：

```python
ans[2 * ncur_len + i] = res[i] - ans[i] - ans[ncur_len + i]

```

这里的 `res[i]` 是全频段点乘结果（频域），而 `ans[i]` 和 `ans[ncur_len + i]` 是已经解出的两个时域分支。

**这个减法 `res[i] - ans[i] - ans[ncur_len + i]`，本质上就是手写代入并化简了 IFFT 逆矩阵的其中一行！**

---

### **对比：手写递归 vs 显式 FWT+IFFT**

两者的逻辑对应关系如下：

| 分治递归代码（你的代码） | 显式 FWT + IFFT 流程 | 频域/信号学含义 |
| --- | --- | --- |
| 构造 `w1`, `w2` 的加法组合 | `FWT(a)`, `FWT(b)` | **正变换 (FFT)**：将时域信号投影到频域基底 |
| `cur_len == 1` 时的 `x1[0] * x2[0]` | `C[i] = A[i] * B[i]` | **频域点乘**：两信号在特定频率上的响应相乘 |
| 递归返回时的 `res - ans0 - ans1` | `IFWT(C)` | **逆变换 (IFFT)**：用逆矩阵将频域合成回时域 |

所以你的直觉完全正确：**这段代码本质上就是把 FFT 投影、频域点乘、IFFT 逆变换这三个步骤，通过递归树的形式隐式地揉在了一起。**