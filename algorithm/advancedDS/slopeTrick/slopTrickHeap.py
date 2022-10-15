# https://www.cnblogs.com/wyzwyz/p/14038855.html
# https://leetcode.cn/problems/NfY1m5/submissions/

import heapq
def slopTrick(ls):
    ql,qr = [],[]
    n = len(ls)
    lenN = [ls[i][1]-ls[i][0] for i in range(n)]
    heapq.heappush(ql, -ls[0][0])
    heapq.heappush(qr, ls[0][0])
    ans = 0 
    addl,addr = 0,0
    for i in range(1,n):
        addl -= lenN[i]
        addr += lenN[i-1]
        L = -ql[0] + addl
        R = qr[0] + addr
        if ls[i][0]<L:
            ans += L-ls[i][0]
            heapq.heappop(ql)
            heapq.heappush(ql,-ls[i][0] + addl)
            heapq.heappush(ql,-ls[i][0] + addl)
            heapq.heappush(qr,L -addr)
        elif ls[i][0] >R:
            ans += ls[i][0] - R 
            heapq.heappop(qr)
            heapq.heappush(qr, ls[i][0] -addr)
            heapq.heappush(qr,ls[i][0] - addr)
            heapq.heappush(ql,-R+addl)
        else:
            heapq.heappush(ql,-ls[i][0] + addl)
            heapq.heappush(qr, ls[i][0]-addr)
        #print(ans,addl,addr,L,R)
    return ans


class Solution(object):
    def buildBridge(self, num, wood):
        """
        :type num: int
        :type wood: List[List[int]]
        :rtype: int
        """
        return slopTrick(wood)
    
re =Solution().buildBridge(10, [[1,5],[1,1],[10,10],[6,7],[7,8]])
#re =Solution().buildBridge(8, [[2,8],[6,7],[2,4]])
print(re)