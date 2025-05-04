
# 
直接贪心匹配是错误的，必须选出所有对象一一匹配
如果直接贪心选择的话， 有可能使用worker直接匹配
Worker:   1   5   6
Task :    5   5   6
pill 1
strength :4

如果先匹配worker,再用药，只能匹配2个


Worker:   1   5   6  
Task :    5   41  45
pill 2
strength :40

如果先匹配worker,不行就用药的话，这样也只能匹配2个