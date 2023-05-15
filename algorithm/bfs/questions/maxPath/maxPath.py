# https://leetcode.cn/contest/weekly-contest-345/problems/maximum-number-of-moves-in-a-grid/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n  = len(grid),len(grid[0])
        g = [[] for _ in range(m*n)]
        for a in range(m):
            for b in range(n):
                for x,y in (a-1,b+1),(a,b+1),(a+1,b+1):
                    if 0<=x<m and 0<=y<n and grid[x][y]> grid[a][b]:
                        g[a*n+b].append(x*n+y)
        visit = {}
        mx = 0
        def bfs(x):
            if x in visit:
                return  visit[x]
            ret = 0
            for a in g[x]:
                ret = max(ret,bfs(a)+1)
            visit[x] = ret
            return ret
        for i in range(0,m*n,n):
            mx = max(mx,bfs(i))
        return mx       
            



matrix = [[1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068],[1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118]]
#matrix= [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
re =Solution().maxMoves(matrix)
print(re)