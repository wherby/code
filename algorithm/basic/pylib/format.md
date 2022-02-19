# format 

# format 保留4位小数
res=1
res =format(res,'.4f')
print(res)

Type "help", "copyright", "credits" or "license" for more information.
>>> res=1
>>> res =format(res,'.4f')
>>> print(res)
1.0000


# format binary
>>> a =2
>>> '{:08b}'.format(a)
'00000010'
>>> '{:032b}'.format(a) 
'00000000000000000000000000000010'