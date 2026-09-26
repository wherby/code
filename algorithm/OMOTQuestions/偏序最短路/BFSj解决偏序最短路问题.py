# https://leetcode.cn/problems/minimum-moves-to-clean-the-classroom/description/?envType=daily-question&envId=2026-09-01
# 这里有多维变量的最短路问题，如果用dijstra 的话，在(step,enegy) 这个偏序的问题上就不能直接判断， 因为形成的 step 和 enegy 两个因子不是严格的可排序变量
# 所以需要用BFS 把 step这个顺序转换为BFS 的顺序解决，然后只用enegy 来做剪枝
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def minMoves(self, mtx: List[str], energy: int) -> int:
        m,n = len(mtx),len(mtx[0])
        ls =[]
        start =(-1,-1)
        for i in range(m):
            for j in range(n):
                a= mtx[i][j]
                if a =="S":
                    start = (i,j)
                if a =="L":
                    ls.append((i,j))
        odic ={(x,y):i for i,(x,y) in enumerate(ls)}
        visit=defaultdict(lambda :-1)
        cand = [(start[0],start[1],0,energy)]
        cnt = 0
        visit[(start[0],start[1],0)]=energy
        while cand:
            tmp = []
            for x,y,state,en in cand:
                if visit[(x,y,state)] > en:
                    continue
                visit[(x,y,state,en)] = 1 
                if state ==(1<<len(ls))-1:
                    return cnt
                if en>0:
                    for nx,ny in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
                        if 0<=nx<m and 0<=ny<n and mtx[nx][ny] !="X":
                            nstate= state
                            nen = en-1
                            if (nx,ny) in odic:
                                nstate = state |(1<<odic[(nx,ny)])
                            if mtx[nx][ny] == "R":
                                nen = energy
                            if visit[(nx,ny,nstate)]<nen:
                                visit[(nx,ny,nstate)] =nen
                                tmp.append((nx,ny,nstate,nen))
            cand = tmp
            cnt +=1
        return -1

classroom= ["XRXXXRRXXL..RXX.RXR.", "XXR.RR.RR..XX.X.XXXX", "XXR..RX.XX.XRXXRXX.R", "L..XR...XXRRRX..X..X", "X.RXXXRX.XRR.XR..X.R", "RRX.RRX..XXXRR.RLRRR", ".RX.RL.XR...RR..R.XR", "RRXXRR...RRXRRRXR..R", ".R..X..RXXRRR..XRX..", "RX.....RRR.RXR..XLX.", "RRXXRLRR..XXRX.R...R", "R.XX.RXRX..XR.R..RRX", "X.XL.XXRXX......XR.R", ".RXX.XRRRX.RX..XX.XX", "RX....RX.RRRRXR..RXX", "LR..XR......XRX....S", ".XX.R.RXRRXX..RRXR..", "...RXRLXRXRRX..XRX.X", "RXRRR..RXXX..XX.RX.R", ".R..XXL.RRX.X...XRXR"]

re  = Solution().minMoves(classroom, energy = 17)
print(re)