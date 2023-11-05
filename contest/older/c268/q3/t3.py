from collections import defaultdict
from bisect import bisect_right,insort_left,bisect_left
class RangeFreqQuery(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.dic = defaultdict(list)
        for i,a in enumerate(arr):
            self.dic[a].append(i)

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        lidx = bisect_left(self.dic[value],left)
        ridx = bisect_right(self.dic[value],right)
        print(lidx,ridx)
        return ridx -lidx



