

## 不可合并端点的线段树
在[a,mod-a] 这样的flop线段树，如果求线段树的最大点，这时 当前值a是可以用max直接合并的，但是flop时，mod-a不可以用max,min来合并，合并的时候，需要记录最大值，flop最大值，的值和index.
[不可以合并值的线段树处理](accoderusage/不可合并端点的线段树.py)
如果用最大值合并的方式记录的时候也是可以的，对零值需要做特殊处理 E = ( 0,0) 这样保证两个值的最大值都能正确合并
[合并最大值表达](<accoderusage/fix.today_is_gonna_be_a_great_day_zhou_tao_tao_zhou_source_code copy.py>)

## 记录数据影响的线段树
利用每个数字插入队列造成的影响记录线段树更新
[记录数据影响](accoderusage/noUseFunctional.py)