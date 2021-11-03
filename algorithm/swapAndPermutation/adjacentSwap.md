# adjacent swap could count by revert ord pairs 
https://www.youtube.com/watch?v=w2AOhnQkpnw

and a n^2 method 

old : abcd
new : bcda

abcd => a#cd => a##d => a### => ####
    1         1      1       0

用new字符串的首字符带入old字符串使得原字符串的那个字符做交换到首字符，把原字符标为# 表示已经处理成功 这样来计算逆数对