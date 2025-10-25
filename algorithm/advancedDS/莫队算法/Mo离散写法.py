# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/E?source=facebook
# 离散写法的时候需要考虑等于的操作在边界扩展的时候是判断是否有下一个和下一个是否在目标区域内
# 连续的情况，
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#filename = "input/input00.txt"
filename = "input/bohemian_rapsody_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


FILEDEBUG=True

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f


from collections import defaultdict,deque
import math
class node:
    def __init__(self,cur =0,cnt = 0) -> None:
        self.child ={}
        self.cur = cur 
        self.cnt = cnt

class Trie:
    def __init__(self) -> None:
        self.root = node()
        self.idx = 0
    
    def insert(self,w):
        r = self.root
        for i in w:
            if i not in r.child:
                r.child[i] = node(self.idx)
                self.idx +=1
            r = r.child[i]
            r.cnt +=1
    
    
    def get(self,x):
        r =self.root
        if len(r.child) == 0:
            return -1
        ret = []
        for i in x:
            r =r.child[i]
            ret.append(r.cur)
        return ret

class FreqTracker():
    def __init__(self):
        self.freq = defaultdict(int)
        self.dic = defaultdict(int)
    
    def modify(self, a,delta):
        aF = self.dic[a]
        self.freq[aF] -=1
        naF = aF + delta
        self.dic[a] = naF
        self.freq[naF] +=1
    
    def freqChecker(self):
        ret = acc = -self.freq[0]
        idx = 1
        while idx <=ret:
            acc -= self.freq[idx]
            ret = min(ret,acc+idx)
            idx +=1
        return ret

def resolve():
    N = int(input())
    words = []
    mx = 0
    for _ in range(N):
        words.append(input())
    M = int(input())
    qrs = defaultdict(list)


    for _ in range(M):
        f,t,k = list(map(lambda x: int(x),input().split()))
        qrs[k].append((f-1,t-1))
    hst = []
    tre =Trie()
    mxlen = 0
    for word in words:
        word = word[::-1]
        tre.insert(word)
        hst.append(tre.get(word))
        mxlen = max(mxlen,len(word))
    cnt = 0
    candList= [[] for _ in range(mxlen+1)]
    for i,hs in enumerate(hst):
        for j in range(len(hs)):
            candList[j].append((hs[j],i))
 

    def MoAlgo(query,l1):
        cand = candList[l1-1]
        #print(query,l1,cand)
        if len(cand) ==0:
            return 0
        block_size = int(math.sqrt(N)) +1
        def mo_cmp(query):
            li,ri, = query[0],query[1] 
            block = li // block_size
            if block %2 == 0:
                return (block,ri)
            else:
                return (block,-ri)
        query.sort(key= mo_cmp)
        frt = FreqTracker()
        cur_li,cur_ri = 0, -1

        def modify(idx,op):
            #print(K,hst[idx],words[idx],k)
            frt.modify(hst[idx][l1-1],op)
            

        cnt = 0
        #print(cand)
        for li, ri in query:
            while cur_li >0 and  cand[cur_li-1][1] >= li  :
                cur_li -=1
                modify(cand[cur_li][1],1)
            while   cur_ri+1 <len(cand) and cand[cur_ri+1][1] <= ri  :
                cur_ri +=1
                modify(cand[cur_ri][1] ,1)
            while cand[cur_li][1] < li and cur_li +1 < len(cand):
                modify(cand[cur_li][1],-1)
                cur_li +=1
            while cand[cur_ri][1] > ri and cur_ri>0:
                modify(cand[cur_ri][1],-1)
                cur_ri -=1
            cnt +=frt.freqChecker()
            #print(li,ri,l1, frt.freqChecker(),cand,cur_li,cur_ri)
        return cnt

    for l1 in range(1,mxlen+1):
        if len(qrs[l1]) ==0:
            continue
        cnt += MoAlgo(qrs[l1],l1)
    
    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)