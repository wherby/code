# https://codeforces.com/gym/106409/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0310/solution/cf106409e.md
# 先对字符串进行处理，找到前半部分和后半部分的字符位置，构造出一个排列，
# 使用相对位置构造一个对应映射，然后用frenwick树求出这个排列的逆序对数量，最后根据题目要求进行计算即可
# 第一部分，左右划分，此时用分配到左半边字符的相对位置，减去左半边的排序后的位置(n // 2 * (n // 2 - 1) // 2)就是 左半边字符冒泡平移到最左边的次数
        # for i in range(n):
        #     if cnt[s[i]]:
        #         former.append(s[i])
        #         cnt[s[i]] -= 1
        #         ans += i
        #     else:
        #         latter.append(s[i])
        
        # ans -= n // 2 * (n // 2 - 1) // 2
# 第2部分用左右半边的对应字符做映射，然后用左边的字符作为排序标准，计算右边字符的逆序对数量，得到右边字符冒泡平移到最右边的次数

import init_setting
from cflibs import *
from lib.fenwicktree import FenwickTree

def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        s = [ord(c) - ord('a') for c in I()]
        n = len(s)
        
        cnt = [0] * 26
        for c in s:
            cnt[c] += 1
        
        for i in range(26):
            cnt[i] //= 2
        
        ans = 0
        
        former = []
        latter = []
        
        for i in range(n):
            if cnt[s[i]]:
                former.append(s[i])
                cnt[s[i]] -= 1
                ans += i
            else:
                latter.append(s[i])
        
        ans -= n // 2 * (n // 2 - 1) // 2
        
        pos1 = [[] for _ in range(26)]
        for i in range(n // 2):
            pos1[former[i]].append(i)
        
        pos2 = [[] for _ in range(26)]
        for i in range(n // 2):
            pos2[latter[i]].append(i)
        
        perm = [0] * (n // 2)
        
        for i in range(26):
            for x, y in zip(pos1[i], pos2[i]):
                perm[x] = y
        
        fen = FenwickTree(n // 2)
        
        for i in range(n // 2):
            ans += fen.rsum(perm[i] + 1, n // 2 - 1)
            fen.add(perm[i], 1)
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))

if __name__ == "__main__":
    main()