from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        ls = sentence.split(" ")
        biaoT =["!",",","."]
        ls = list(filter(lambda x: len(x.strip())>0,ls))
        ls = list(filter(lambda x:  x[0].isalpha() or (x[0] in biaoT),ls))
        print(ls)
        cnt =0
        
        for item in ls:
            if item.find("-") ==0 or item.find("-") == (len(item)-1) or item.find("-") != item.rfind("-"):
                continue
            if item.find("-") >=0:
                k = item.find("-")
                if (not item[k-1].isalpha()) or (not item[k+1].isalpha()):
                    continue
            hasNum =False
            biao=[]
            for t in item:
                if t  >="0" and t <="9":
                    hasNum=True
                if str(t) in biaoT:
                    biao.append(t)
                #print(t,str(t) in biao,biao)
            if len(biao) > 0 and (item[-1] not in biaoT):
                continue
            if len(biao) >1:
                continue
            if not hasNum:
                cnt +=1
                #print(item)
                #print(biao)
        return cnt



re=Solution().countValidWords(" 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif ")
print(re)