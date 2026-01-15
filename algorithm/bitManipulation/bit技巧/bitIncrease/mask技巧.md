

# MASK 技巧 

## 进位技巧，加1 

https://leetcode.cn/problems/maximum-bitwise-and-after-increment-operations/solutions/3877680/shi-tian-fa-pai-xu-kuai-su-xuan-ze-pytho-3fyt/
https://www.bilibili.com/video/BV1tv6dBME7K/?spm_id_from=333.1387.homepage.video_card.click&vd_source=ca787d3785cbd6247961eba27850fa0c



```python
b  =  target & (~a)
j = b.bit_length()
msk = (1<<j) -1
costs.append((target & msk) - (a & msk))
```

为了使得 a 增长到 target 同样的位上都为1 
```
# j-1 是从高到低第一个 target 是 1 且 x 是 0 的比特位
# target = 10110
#      x = 11010
#            ^
#           j-1
# x 二进制中的高于 j-1 的位不变，其余位增大到和 target 一样
# 上面的例子要把 010 变成 110
```

这里有用的部分是在 target上为1，同时在a 中为0 的最高位（如果target 和 a 中同一位都相等，则这位没有比较必要，如果target的某位为0，此位在a中为0或者1 没有区别） 为了找到最高位，则 用 target &（~a) 取的数字的 bit_length(), 然后用 (1<<j) -1 的到 最高位以后的msk,然后用target&msk - a&msk 得到需要增长的有效位数就好了

基础处理的方式就需要每一位单独计算，并且维护最低位的有效值


## 借位技巧，减一

这时寻找所有原数是1，而target是0 的位置，找到该位借位之后的值，看是否与target完全覆盖，如果是，则是候选项

```python 
        # 2. 计算向下减少的最小代价 (x - x_down)
        cost_down = float('inf')
        # 遍历所有 x 为 1 且 target 为 0 的位作为借位点
        # 优化：只需考虑比缺失最高位 h 更高的位即可
        temp_x = x
        for p in range(x.bit_length()):
            bit = 1 << p
            if (x & bit) and not (target & bit):
                # 构造 x_down: p位变0, 高位保留, 低位全变1
                x_down = ((x >> (p + 1)) << (p + 1)) | (bit - 1)
                # 确保 x_down 仍然包含 target (如果不包含说明此借位点无效)
                if (x_down & target) == target:
                    cost_down = min(cost_down, x - x_down)
```
