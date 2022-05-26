#https://leetcode.cn/problems/falling-squares/
from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ls = [[-1000,10**10,0]]
        ret =[]
        mx =0
        for st,le in positions:
            left,right = st,st+le
            lidx =bisect_left(ls,left,key=lambda x:x[0])
            lidx -=1
            if ls[lidx][1]<=left:
                lidx +=1
            replaced =[]
            if ls[lidx][0]<left:
                a = ls[lidx]
                replaced.append([a[0],left,a[2]]) 
            cmx = ls[lidx][2]
            endIndx = lidx
            while endIndx < len(ls) and ls[endIndx][0]<right:
                #print(endIndx)
                cmx = max(cmx,ls[endIndx][2])
                endIndx +=1
            replaced.append([left,right,cmx+le])
            if ls[endIndx-1][1] != right:
                a = ls[endIndx-1]
                replaced.append([right,a[1],a[2]])
            mx = max(mx,cmx+le)
            ret.append(mx)
            ls[lidx:endIndx] = replaced
        #print(ls,ret)
        return ret 
                
        

a= [[1, 2], [2, 3], [5, 5]]        
re =Solution().fallingSquares(a)
print(re)