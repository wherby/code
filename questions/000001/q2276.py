from sortedcontainers import SortedList
from bisect import bisect_right,bisect_left
## Merge on continue [[1,1][2,2]] will  merge
class Span():
    def __init__(self):
        self.span =SortedList([(-1,-1),(10**10,10**10)])
        self.cnt = 0
    
    def add(self,left,right):
        leftIdx = bisect_left(self.span,(left,0))
        leftIdx -=1
        if self.span[leftIdx][1] <left-1:
            leftIdx +=1
        remove=[]
        endIdx = leftIdx
        while  endIdx < len(self.span) and self.span[endIdx][0] <=right +1:
            remove.append(self.span[endIdx])
            endIdx +=1
        newLeft,newRight = left,right
        for item in remove:
            newLeft = min(newLeft,item[0])
            newRight = max(newRight,item[1])
            self.span.remove(item)
            self.cnt -= item[1]-item[0]+1
        self.span.add((newLeft,newRight))
        self.cnt += newRight-newLeft +1
        
class CountIntervals:

    def __init__(self):
        self.sp =Span()


    def add(self, left: int, right: int) -> None:
        self.sp.add(left,right)

    def count(self) -> int:
        return self.sp.cnt



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()