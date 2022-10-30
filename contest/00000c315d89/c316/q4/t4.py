from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        s11,s12 =SortedList(),SortedList()
        target.sort()
        for a in nums:
            if a %2 ==1:
                s11.add(a)
            else:
                s12.add(a)
        ls1 ,ls2 = [],[]
        for a in target:
            if a %2 ==1:
                ls1.append(a-s11[0])
                s11.remove(s11[0])
            else:
                ls2.append(a -s12[0])
                s12.remove(s12[0])
        #print(ls1,ls2)
        def countls(ls):
            acc,cnt =0,0
            for a in ls:
                if a <0:
                    if acc <=0:
                        cnt -=a 
                    else:
                        cnt -= min(0,a +acc)
                    acc +=a 
                else:
                    if acc >=0:
                        cnt += a 
                    elif a + acc <0:
                        pass
                    else:
                        cnt += a +acc 
                    acc +=a 
            #print(acc,cnt)
            return cnt 
        ls1.extend(ls2)
        
        return (countls(ls1))>>1
        
        
            
        




re =Solution().makeSimilar(nums = [1,2,5], target = [4,1,3])
print(re)