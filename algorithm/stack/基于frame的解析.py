# https://leetcode.cn/problems/brace-expansion-ii/description/?envType=daily-question&envId=2026-09-25
# 这个题目是解析表达式，里面有 "{}"表示每个语义Frame, “,”表示取并集， 默认是笛卡尔积
# 所以这里dfs解析每个Frame， 然后在并集的时候在Frame 内计算，这时就需要在当前Frame里保存两个部分，已经处理的结果和当前块
# 由于存在嵌套结构，所以当前块并不是一个变量，而是变量集合
# “," 反而是当前快结束的标志



class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0 

        def dfs():
            nonlocal i 
            res = set()
            cur = {""}

            while i < len(expression):
                ch = expression[i]
                i +=1

                if ch =="}":
                    break 
                if ch ==",":
                    res |= cur 
                    cur = {""}
                elif ch =="{":
                    sub_res = dfs()
                    cur = {s + t for s in cur for t in sub_res}
                else:
                    cur = {s + ch for s in cur}
                #print(res,cur)
            return res | cur 
        return sorted(dfs())

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []  # 用于模拟计算机的递归
        res = set()
        cur = {""}  # 加个空串，简化后续判断逻辑

        for ch in expression:
            if ch.isalpha():  # 字母
                cur = {s + ch for s in cur}  # 把 ch 添加到 cur 每个字符串的末尾
            elif ch == ',':  # 取并集
                res |= cur  # 把 cur 中的字符串都添加到 res 中
                cur = {""}
            elif ch == '{':  # 递
                # 模拟递归
                stack.append((res, cur))  # 递归前，把局部变量 res 和 cur 保存到栈中
                res = set()  # 递归，初始化 res 和 cur
                cur = {""}
            else:  # 归
                sub_res = res | cur  # 递归结束，返回值为 sub_res
                res, cur = stack.pop()  # 从栈中恢复递归之前保存的局部变量
                cur = {s + t for s in cur for t in sub_res}  # 计算 cur 和 sub_res 的笛卡尔积

        return sorted(res | cur)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/brace-expansion-ii/solutions/4031376/liang-chong-xie-fa-di-gui-yong-zhan-mo-n-n2do/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。