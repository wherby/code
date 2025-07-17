# https://codeforces.com/problemset/problem/2048/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0716/solution/cf2048e.md

import sys
import os 
# 获取当前脚本的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# # 构造到目标库目录的路径
# # 假设 common_utils.py 在 ../another_folder/my_library
parent_dir = os.path.dirname(current_dir)

# library_path = os.path.join(parent_dir, 'lib')

# sys.path.append(library_path)

sys.path.append(parent_dir )
print(sys.path)
from lib.cflibs import *
def main():
    t = II()
    outs = []

    for _ in range(t):
        n, m = MII()
        if m >= 2 * n: outs.append('NO')
        else:
            outs.append('YES')
            for i in range(2 * n):
                outs.append(' '.join(str((i + j) % (2 * n) // 2 + 1) for j in range(m)))

    print('\n'.join(outs))

main()