# 仿射运算不具有交换性，需要对当前值作为右值计算，对左值进行仿射映射

from collections import deque
mod = 10**9+7 
#mod = 998244353

def queueExe(st:deque,eval):
    while len(st)>2:
        right = st.popleft()
        op = st.popleft()
        left = st.popleft()
        st.appendleft(eval(left,right,op))
    return st[0]


def basicEval(left,right, op):
    if op =="+":
        return left + right
    elif op =="-":
        return left - right
    elif op == "/":
        return left*pow(right,-1,mod)%mod
    return left *right




def affineTEveal(x, y, op):
    # 对新值 x 进行仿射变换
    if op == "+":
        y = y + mod      
    elif op == "-":
        y = (-y)%mod + mod    
    elif op == "/":
        y = mod * pow(y, -1, mod)  
    else:  # "*"
        y = y * mod      
    
    # 然后将变换后的 x 与积累值 y 进行运算
    xa, xb = divmod(x, mod)
    ya, yb = divmod(y, mod)
    a = ya * xa % mod
    b = (xb*ya + yb) % mod
    return a * mod + b



if __name__ == '__main__':
    import random
    from itertools import zip_longest
    N = 500

    st = [random.randint(1,10000) for _ in range(N)]
    opv= "+*/-"
    ops = [opv[random.randint(0,3)] for _ in range(N-1)]
    result = []
    for num, op in zip_longest(st, ops, fillvalue=None):
        result.append(num)
        if op is not None:
            result.append(op)
    ls= deque(result)
    
    #ls= [47, '*', 23, '*', 36, '*', 90, '*', 96, '+', 81, '*', 16, '+', 59, '+', 28, '+', 66, '+', 43, '*', 67, '*', 7, '+', 59, '*', 10, '+', 10, '*', 96, '+', 55, '+', 55, '*', 79]
    #print(ls)
    x1 = queueExe(deque(ls),basicEval)
    #print(ls)
    ls2 = deque(ls)
    ls2[-1] += mod 
    #print(ls2)
    x2 = queueExe(deque(ls2),affineTEveal)
    #print(x1,x2)
    print(x1%mod,x2%mod)
        # 验证
    if x1 % mod == x2 % mod:
        print("\n✅ 验证通过：在当前模数下，仿射变换结果与数值计算结果一致。")
    else:
        print(f"\n❌ 验证失败：结果不一致。 (差异: {x1 % mod - x2 % mod})")
def testops():
    # 先用简单表达式调试
    test_cases = [
        [2, '*', 3],           # 6
        [2, '+', 3],           # 5  
        [6, '-', 2],           # 4
        [6, '/', 2],           # 3
    ]

    for test in test_cases:
        print(f"\n测试: {test}")
        x1 = queueExe(test.copy(), basicEval)
        test_affine = test.copy()
        test_affine[-1] += mod
        x2 = queueExe(test_affine, affineTEveal)
        print(f"基础: {x1 % mod}, 仿射: {x2 % mod}, 一致: {x1 % mod == x2 % mod}")

