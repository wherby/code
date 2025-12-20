
# https://leetcode.cn/problems/find-all-people-with-secret
# 解决这个问题的时候。先标记连接，如果下一阶段开始，如果标记不起作用，则撤回标记
from typing import List, Tuple, Optional


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parents = list(range(n))
        parents[firstPerson] = 0

        def find(x):
            if parents[x] != x and parents[x] != 0:
                parents[x] = find(parents[x])
            return parents[x]

        last_t = 0
        reffered = set()
        for a, b, t in sorted(meetings, key=lambda x: x[2]):
            if t > last_t:
                last_t = t
                for i in reffered:
                    if find(i) != 0:
                        parents[i] = i
                reffered = set()
            if (fa:=find(a)) == 0:
                parents[find(b)] = 0
                parents[b] = 0
            elif (fb:=find(b)) == 0:
                parents[find(a)] = 0
                parents[a] = 0
            else:
                parents[fa] = fb
                reffered.add(a)
                reffered.add(b)

        return [i for i in range(n) if find(i) == 0]