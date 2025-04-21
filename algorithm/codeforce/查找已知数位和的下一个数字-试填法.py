# 生成大于数字X的数位和为N 的值
# 
# 试填法： 先用X的数位从高到低试填，如果N用尽，则选择最小高位找一个进位 则填入值试比X大（flg ==True)
#         如果填完之后，当前值没比X大，如果N不为0，则在最小位数上加1，再按照从小到大补齐用完N 
#                                 如果N为0，则要做一个进位操作，从小到大抹去低位的9

# https://codeforces.com/problemset/problem/509/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0416/solution/cf509c.md


from cflibs import *

def main():
    cur = [0] * 400

    t = II()
    outs = []

    for _ in range(t):
        n = II()
        ncur = [0] * 400
        
        flg = False
        for i in range(400):
            if n >= cur[i]:
                n -= cur[i]
                ncur[i] = cur[i]
            else:
                flg = True
                for j in range(i - 1, -1, -1):
                    if n and ncur[j] != 9:
                        ncur[j] += 1
                        n -= 1
                        break
                    else:
                        n += ncur[j]
                        ncur[j] = 0
                break
        #确保当前的值大于前一个值 flg =>true
        if not flg:
            if n:
                ncur[399] += 1
                n -= 1
            else:
                for j in range(399, -1, -1):
                    if n and ncur[j] != 9:
                        ncur[j] += 1
                        n -= 1
                        break
                    else:
                        n += ncur[j]
                        ncur[j] = 0
        #从小到大，使得最低位尽量使用完数字
        for j in range(399, -1, -1):
            v = fmin(n, 9 - ncur[j])
            ncur[j] += v
            n -= v
        
        cur = ncur
        for i in range(400):
            if ncur[i]:
                outs.append(''.join(map(str, (cur[j] for j in range(i, 400)))))
                break

    print('\n'.join(outs))

