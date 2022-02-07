
class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        mx = 1000000000000000000000000000000
        s1,s2 = targetSeconds //60, targetSeconds%60
        cand= []
        if s1 <100:
            if s1 !=0:
                cand.append(str(s1)+ "{:02}".format(s2)  )
            else:
                cand.append(str(s2)  )
        if s2 <40 and s1 >0:
            s1,s2 = s1-1,s2+60
        if s1 !=0:
            cand.append(str(s1)+ "{:02}".format(s2)  )
        else:
            cand.append(str(s2)  )
        # if use second:
        print(cand)
        def getCnt(targetSeconds):
            nonlocal mx
            cnt =0
            state = str(startAt)
            tst = str(targetSeconds)
            for a in tst:
                if a !=state:
                    cnt +=moveCost +pushCost
                    state =a
                else:
                    cnt +=pushCost
                #print(cnt,a,startAt)
            mx = min(mx,cnt)
        for c in cand:
            getCnt(c)
        return mx

re = Solution().minCostSetTime(startAt = 1, moveCost = 9403, pushCost = 9402, targetSeconds = 6008)
print(re)

