# https://leetcode.cn/problems/maximum-capacity-within-budget/description/
from typing import List, Tuple, Optional



class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        a = [(cost, cap) for cost, cap in zip(costs, capacity) if cost < budget]
        a.sort(key=lambda p: p[0])

        st = [(0, 0)]  # 栈底加个哨兵
        ans = 0
        for cost, cap in a:
            while cost + st[-1][0] >= budget:
                st.pop()  # 弹出太贵的机器
            ans = max(ans, cap + st[-1][1])
            if cap > st[-1][1]:
                st.append((cost, cap))
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-capacity-within-budget/solutions/3883296/pai-xu-qian-zhui-zui-da-zhi-dan-diao-zha-zz22/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。