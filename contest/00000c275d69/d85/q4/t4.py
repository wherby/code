from sortedcontainers import SortedDict,SortedList
import heapq
class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        """
        :type nums: List[int]
        :type removeQueries: List[int]
        :rtype: List[int]
        """
        n = len(nums) 
        sm = sum(nums)
        sl = SortedList([(0,n-1,sm),(n,n+2,0)])
        dicRm ={}
        st =[]
        heapq.heappush(st,(-sm,0,n-1))
        ls = [0]*(n+1)
        for i,a in enumerate(nums):
            ls[i+1] = ls[i] + a 
        ret = []
        for i,a in enumerate(removeQueries):
            k  = sl.bisect_right((a,a,a))
            if a == sl[k][0]:
                item = sl[k]
            else:
                item = sl[k-1]
            dicRm[(-item[2],item[0],item[1])] = 1
            left,right,all =item
            #print(left,right,all,st,sl,k,a)
            item1 = (left,left,0)
            if a-1>=left:
                item1 = (left,a-1,ls[a]-ls[left])
            item2 = (right,right,0)
            if a+1 <=right:
                
                item2 = (a+1,right,ls[right+1]-ls[a+1])
            sl.remove(item)
            
            sl.add(item1)
            sl.add(item2)
            heapq.heappush(st,(-item1[2],item1[0],item1[1]))
            heapq.heappush(st,(-item2[2],item2[0],item2[1]))
            big = st[0]
            while big in dicRm:
                heapq.heappop(st)
                big = st[0]
            ret.append(-big[0])
        return ret
        





re =Solution().maximumSegmentSum(nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1])
print(re)