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
        cand =[]
        st = []
        for i,a in enumerate(nums):
            heapq.heappush(st,(abs(a),i))
        while 2**len(cand) < k:
            a,b = heapq.heappop(st)
            cand.append((a,b))
        print(len(cand),k)
        alls = []
        res =[]
        arr = cand
        cnt =0
        alldic ={}
        def allCombination(idx):
            nonlocal cnt
            n = len(arr)
            if idx ==n :
                cnt +=1
                keys = []
                vals = 0
                for a,b in res:
                    keys.append(b)
                    vals +=a 
                alldic[tuple(sorted(keys))] = vals
                return
            allCombination(idx+1) # without idx
            res.append(arr[idx])  # add idx
            allCombination(idx+1) # with idx
            res.pop()             # recover back
        allCombination(0)
        m  = min(len(nums),k //len(nums)+1)
        #print(m,len(nums))
        ls =[i for i in range(len(nums))]
        acc =0
        for j in range(m):
            for x in itertools.combinations(ls,j):
                acc +=1
                if acc > 20000:
                    break
                tm = 0
                for b in x:
                    tm += abs(nums[b])
                alldic[tuple(x)] = tm
        alls.sort()
        #print(alldic)
        vals  = list(alldic.values())
        vals.sort()
        
        return sum(aboveZero) -vals[k-1]



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