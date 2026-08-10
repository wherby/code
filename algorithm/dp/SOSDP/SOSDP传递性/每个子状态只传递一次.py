# https://codeforces.com/gym/106631/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0803/solution/cf106631g.md
# algorithm/codeforce/dp/SOSDP/SOS标记传递.py
# 这里从最低位到最高位，也可以从最高位到最低位也可以

def state(stat):
    res =[stat]
    for i in range(30):
        for a in res:
            if (1<<i) &a:
                res.append( a ^ (1<<i))
    return res 

print([bin(a) for a in state(30)])
print([bin(a) for a in state(10)])