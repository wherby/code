# https://leetcode.cn/problems/reverse-string-ii/solutions/3056217/jian-dan-ti-jian-dan-zuo-pythonjavaccgoj-ig15/?envType=daily-question&envId=2025-01-31
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from apptimer import timer_func

class Solution:
    @timer_func
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), k * 2):
            s[i: i + k] = s[i: i + k][::-1]  # 右端点自动和 n 取最小值
        return  ''.join(s)
    @timer_func
    def reverseStr2(self, s: str, k: int) -> str:
        n=len(s)
        ret =""
        for i in range(0,n,2*k):
            t = s[i:i+2*k]
            ret += t[:k][::-1]
            ret += t[k:]
            #print(len(ret))
        return ret
    @timer_func
    def reverseStr3(self, s: str, k: int) -> str:
        n=len(s)
        ret =[]
        for i in range(0,n,2*k):
            t1=""
            t = s[i:i+2*k]
            t1 += t[:k][::-1]
            t1 += t[k:]
            ret.append(t1)
            #print(len(ret))
        return "".join(ret)

str1 = "1234568"*10000000
#str1= "123456"*10
re1 =Solution().reverseStr(str1,4)
re2= Solution().reverseStr2(str1,4)
re3= Solution().reverseStr3(str1,4)
print(re1==re2,re2==re3)
#print(re1,re2,re3)
#print(re)