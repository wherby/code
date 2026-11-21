# https://leetcode.cn/problems/count-mentions-per-user/description/?envType=daily-question&envId=2025-12-12
# 对于 offline 和here 的处理，求here的时候先把 offline造成的影响去掉，变成All， 然后把 here求取事件和 offline影响的事件加入事件序列
# 然后在事件序列中处理 offline造成的影响， 而offline造成的影响也是先弃后取，只关注 offline期间 here的变动情况
from typing import List, Tuple, Optional

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans = [0] * numberOfUsers
        es = []  # (timestamp, type, id)
        all = 0
        for type_, timestamp, mention in events:
            cur_t = int(timestamp)  # 当前时间
            if type_[0] == 'O':  # 离线
                i = int(mention)
                es.append((cur_t, 1, i))
                es.append((cur_t + 60, -1, i))
            elif mention[0] == 'A':  # @所有人
                all += 1
            elif mention[0] == 'H':  # @所有在线用户
                all += 1
                es.append((cur_t, 2, -1))
            else:  # @id
                for s in mention.split():
                    ans[int(s[2:])] += 1

        es.sort()

        here = 0
        for _, type_, i in es:
            if type_ == 2:
                here += 1
            else:
                # 注意 HERE 排在后面，还没有计入发生在此刻的 HERE 消息
                ans[i] += type_ * here  # type=1 是加，-1 是减

        for i in range(numberOfUsers):
            ans[i] += all
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-mentions-per-user/solutions/3057699/an-zhao-shi-jian-chuo-fen-zu-mo-ni-by-en-w77b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。