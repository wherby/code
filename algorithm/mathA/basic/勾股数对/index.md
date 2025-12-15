
# 特性

https://zhuanlan.zhihu.com/p/1978057341963368012
定义满足 
 的勾股数组 
 为本原勾股数组（Primitive Pythagorean Triples，PPT）

a**2 + b**2 = c**2  设其中 b 是偶数，a,c是奇数

a**2 = (c-b) *(c+b) 对于本源勾股数，可以推论得到 c-b, c+b 都是平方数 等于 v**2,u**2 
则 a = u*v b =(u**2 -v**2 )//2. c =(u**2 + v**2 )//2 
而a是奇数，则u,v为奇数
 只需，gcd(u,v) ==1 

a =3,b =4,c = 5 ||  u =3,v=1
a =5,b=12,c =13 || u = 5,v =1 
a =15,b =8,c =17 || u=5,v=3
a=21,b =20,c=29  || u =7,v =3 

然而，求u,v只需要满足 v<u and gcd(u,v) =1 就能找到对应的本源勾股数。则可以通过数论
[数论解法](数论.py)