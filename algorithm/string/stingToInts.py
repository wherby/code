# string 所有int分割的和的组合
import functools
@functools.cache
def gen_ints(s:str): return {0} if not s else set(int(s[:i + 1]) + nn for i in range(len(s)) for nn in gen_ints(s[i + 1:]))

re=gen_ints("1204")
print(re)