from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList




def  strA(st1):
    st= []
    for a in st1:
        while  len(st)>=2 and  a == st[-2] =="0":
            st.pop()
        st.append(a)
    print(st)
            
strA("101010101111")

[1]
[1,0]
[1,0,1]
[1,0,0]
[1,0,0,1]
[1,0,0,]
[1,0]
[1,0,0]
[1,0,0,1]
[1,0,0,]
[1,0,0,1,1,1,1,]