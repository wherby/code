import heapq
import itertools
class Solution(object):
    def kSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        aboveZero = []
        lessThanZero =[]
        for a in nums:
            if a >=0:
                aboveZero.append(a)
            else:
                lessThanZero.append(a)
        aboveZero.sort()
        lessThanZero.sort(reverse=True)
        st = []
        for a in nums:
            st.append(abs(a))
        st.sort()
        cand=[0]
        for x in st[:k]:
            q =[x+ y for y in cand]
            cand  = cand + q 
            cand.sort()
            cand = cand[:k]
        return sum(aboveZero) -cand[-1]



# re =Solution().kSum(nums = [1000,1001,1002,1003,1004,1005,1006,1007,1008,1009], k = 10)
# print(re)
# re =Solution().kSum(nums = [1,-2,3,4,-10,12], k = 16)
# print(re)
# nums=[-731575093,-236261761,-759616099,-167023428,-350754181,385948503,-770162071,-60277982,-680948276,696763878,-959139513,562428318,1951742,463221991,15174891,693641656,-171514964,-676270856,862700558,-194013414]
# k=504
nums=[153123449,-974739108,-408679566,-996444415,-978921261,805907128,-102259288,-397930077,51033052,-193994032,158654659,-486195972,-294264190,-65262667,375941242,-890038230,315970860,403847239,-32469129,-350561293,192113942,794248972,-632675681,434029943,746632801,500370163,164413366,346449701,473890512]
k=1906
re =Solution().kSum(nums , k )
print(re)