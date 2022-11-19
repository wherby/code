from typing import List, Tuple, Optional

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        i = cap = 0
        while True:
            i += 1
            if i < 10:
                tail_len = 5  # 结尾的长度
            elif i < 100:
                if i == 10: cap -= 9  # 前面的结尾的长度都 +1，那么容量就要减小
                tail_len = 7
            elif i < 1000:
                if i == 100: cap -= 99
                tail_len = 9
            else:
                if i == 1000: cap -= 999
                tail_len = 11
            if tail_len >= limit: return []  # cap 无法增大，寄
            cap += limit - tail_len
            if cap < len(message): continue  # 容量没有达到，继续枚举

            ans, k = [], 0
            for j in range(1, i + 1):
                tail = f"<{j}/{i}>"
                if j == i:
                    ans.append(message[k:] + tail)
                else:
                    m = limit - len(tail)
                    ans.append(message[k: k + m] + tail)
                    k += m
            return ans
