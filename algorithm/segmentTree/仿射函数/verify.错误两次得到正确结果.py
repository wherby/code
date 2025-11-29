# 这里初始值设置错误，并且 仿射函数 顺序错误，但是结果正确

from collections import defaultdict,deque
mod = 10**9+7 
#mod = 998244353

def stackExe(st,eval):
    while len(st)>2:
        a = st.pop()
        op = st.pop()
        b = st.pop()
        st.append(eval(a,b,op))
    return st[0]


def basicEval(a,b, op):
    if op =="+":
        return b + a 
    return b*a



def affineTEveal(x,y,op):
    
    if op == "+":
        x = x+mod
    else:
        x = x*mod
    xa,xb= divmod(x,mod)
    ya,yb = divmod(y,mod)
    a = xa * ya % mod
    b = (xa * yb + xb) % mod
    return a * mod + b



if __name__ == '__main__':
    import random
    from itertools import zip_longest
    N = 220

    st = [random.randint(1,100) for _ in range(N)]
    opv= "+*"
    ops = [opv[random.randint(0,1)] for _ in range(N-1)]
    result = []
    for num, op in zip_longest(st, ops, fillvalue=None):
        result.append(num)
        if op is not None:
            result.append(op)
    ls= deque(result)
    
    #ls= [47, '*', 23, '*', 36, '*', 90, '*', 96, '+', 81, '*', 16, '+', 59, '+', 28, '+', 66, '+', 43, '*', 67, '*', 7, '+', 59, '*', 10, '+', 10, '*', 96, '+', 55, '+', 55, '*', 79]
    print(ls)
    x1 = stackExe(list(ls),basicEval)
    print(ls)
    ls2 = deque(ls)
    ls2[0] += mod 
    print(ls2)
    x2 = stackExe(list(ls2),affineTEveal)
    print(x1,x2)
    print(x1%mod,x2%mod)
        # 验证
    if x1 % mod == x2 % mod:
        print("\n✅ 验证通过：在当前模数下，仿射变换结果与数值计算结果一致。")
    else:
        print(f"\n❌ 验证失败：结果不一致。 (差异: {x1 % mod - x2 % mod})")

