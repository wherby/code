
# 斐波那契矩阵形式 
a = [[1,1],[1,0]]

[矩阵表达](verify.py)

# 初始项不是 1,2 是 A，B 的递推公式
[初始项为 A,B](verify.py)


# 高阶递推 解决 F[n] =F[n-1]**p * F[n-2]**q
![高阶递推](pic/高阶递推.png)
![高阶递推2 ](pic/高阶递推2.png)
![高阶递推3](pic/高阶递推3.png)

# 三阶递推 解决 F[n] =F[n-1]**p * F[n-2]**q * C 
![三阶递推](pic/三阶递推.png)
![三阶递推2](pic/三阶递推2.png)
![三阶递推3](pic/三阶递推3.png)

## 三阶递推系数计算
![alt text](pic/三维系数求取.png)
![alt text](pic/三维系数求取2.png)
![alt text](pic/三维系数求取3.png)
![alt text](pic/三维系数求取4.png)

## 系数偏移问题

![alt text](pic/系数偏移问题.png)
![alt text](pic/系数偏移问题2.png)
![alt text](pic/系数偏移问题3.png)
![alt text](pic/系数偏移问题4.png)

其实很简单，2阶和三阶的系数偏移是因为在计算的时候二阶用的N次方，三阶计算用的是N-1次方，所以三阶用第一行的值，二阶用第二行的值