#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
#filename = "input/bohemian_rapsody_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


FILEDEBUG=False

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

    def MoAlgo(query,K):
        block_size = int(math.sqrt(mxlen)) +1
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
            if len(words[idx]) <K:
                return 
            #print(K,hst[idx],words[idx],k)
            frt.modify(hst[idx][K-1],op)
            

        cnt = 0

        for li, ri in query:
            while cur_li > li:
                cur_li -=1
                modify(cur_li,1)
            while cur_ri < ri:
                cur_ri +=1
                modify(cur_ri,1)
            while cur_li < li:
                modify(cur_li,-1)
                cur_li +=1
            while cur_ri > ri:
                modify(cur_ri,-1)
                cur_ri -=1
            cnt +=frt.freqChecker()
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