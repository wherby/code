from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from collections import Counter
from sortedcontainers import SortedDict,SortedList
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        st =[]
        pc = set(positive_feedback)
        nc = set(negative_feedback)
        for i,record in zip(student_id,report):
            acc =0
            ls = record.split(" ")
            for a in ls:
                if a in pc:
                    acc +=3
                if a in nc:
                    acc -=1
            heapq.heappush(st,(-acc,i))
        ret =[]
        #print(st)
        for _ in range(k):
            acc,i = heapq.heappop(st)
            ret.append(i)
        return ret





re =Solution().topStudents(["fkeofjpc","qq","iio"],["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"],["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"],[96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263],3)
print(re)