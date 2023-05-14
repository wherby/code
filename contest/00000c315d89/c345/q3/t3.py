from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n  = len(grid),len(grid[0])
        visit={}
        mp = [[0]*n for _ in range(m)]
        def visit(x1,y1):
            st = [(x1,y1)]
            step =-1
            while st:
                tp=[]
                for a,b in st:
                    if (a,b) in visit:continue
                    visit[(a,b)]=1
                    for x,y in (a-1,b+1),(a,b+1),(a+1,b+1):
                        if 0<=x<m and 0<=y<n and (x,y) not in visit and grid[x][y]> grid[a][b]:
                            tp.append([x,y])
                step +=1
                st = tp
            #print(st)
        return step



matrix = [[1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068],[1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118]]

re =Solution().maxMoves(matrix)
print(re)