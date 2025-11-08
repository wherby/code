from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class BQue:
    def __init__(self,k):
        self.k = k 
        self.left= SortedList([])
        self.right = SortedList([])
        self.leftV = 0
        self.rightV=0 
    
    def getV(self, a):
        return a[0]*a[1]

    def add(self,a):
        self.right.add(a)

        self.rightV +=self.getV(a)
        self.adjust()
    
    def remove(self,a):
        if a >= self.right[0]:
            self.right.remove(a)
            self.rightV -=self.getV(a)
        else:
            self.left.remove(a)
            self.leftV -=self.getV(a)
        self.adjust()
    
    def adjust(self):
        while len(self.right) < self.k and len(self.left):
            b = self.left.pop()
            self.leftV -= self.getV(b)
            self.right.add(b)
            self.rightV +=self.getV(b)
        while len(self.right) > self.k:
            b = self.right[0]
            self.rightV -= self.getV(b)
            self.right.remove(b)
            self.left.add(b)
            self.leftV+=self.getV(b)


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ret = []
        c = Counter()
        bq = BQue(x)
        for i,a in enumerate(nums):
            b= c[a]
            c[a] +=1
            bq.add((c[a],a))
            if b >0:
                
                bq.remove((b,a))
            
            if i >= k:
                e = nums[i-k]
                f = c[e]
                bq.remove((f,e))
                bq.add((f-1,e))
                c[e]-=1
            if i >=k-1:
                #print(bq,b,a,bq.left,bq.right)
                ret.append(bq.rightV)
        return ret


re = Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2)
print(re)