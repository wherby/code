# https://codeforces.com/gym/100384/attachments/download/2305/2014-zimnyaya-shkola-po-programmirovaniu-harkov-dyen-9-v-nyespirnyy-uniorskaya-liga-en.pdf
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0912/solution/cf100384h.md
# 构造题，2进制延长
# 在无限的数轴 0-index 的时候，把偶数的点都填a， 然后把数轴奇数的点取出，构成新的0-index数轴，然后把新数轴的偶数点填b,循环处理
# Lets look at the string of characters. We can say that the line s1s2 . . . sn is a repetition, if there are two identical
# substrings that follows one after another. That is, if for some i and k (i, k > 0, i + 2k − 1 ≤ n)) following expression
# si = si+k, si+1 = si+k+1, . . . , si+k−1 = si+2k−1 is true.
# Find lexicographically minimal string of length n without repetition

import init_setting
from cflibs import *
def main():
    n = II()
    print(''.join(chr(ord('a') + (i & -i).bit_length() - 1) for i in range(1, n + 1)))