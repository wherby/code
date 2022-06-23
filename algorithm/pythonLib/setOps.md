# Set operation

##
https://realpython.com/python-sets/

>>> x = {'foo', 'bar', 'baz'}
>>> x.add('qux')
>>> x
{'bar', 'baz', 'foo', 'qux'}


>>> x = {'foo', 'bar', 'baz'}
>>> x.remove('baz')
>>> x
{'bar', 'foo'}
>>> x.remove('qux')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    x.remove('qux')
KeyError: 'qux'

>>> x = {'foo', 'bar', 'baz'}
>>> x.discard('baz')
>>> x
{'bar', 'foo'}
>>> x.discard('qux')
>>> x
{'bar', 'foo'}

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}
>>> x1 | x2
{'baz', 'quux', 'qux', 'bar', 'foo'}
>>> x1.union(x2)
{'baz', 'quux', 'qux', 'bar', 'foo'}


>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}
>>> x1.intersection(x2)
{'baz'}
>>> x1 & x2
{'baz'}


>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}
>>> x1.difference(x2)
{'foo', 'bar'}
>>> x1 - x2
{'foo', 'bar'}

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}
>>> x1.symmetric_difference(x2)
{'foo', 'qux', 'quux', 'bar'}
>>> x1 ^ x2
{'foo', 'qux', 'quux', 'bar'}

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}
>>> x1.isdisjoint(x2)
False
>>> x2 - {'baz'}
{'quux', 'qux'}
>>> x1.isdisjoint(x2 - {'baz'})
True


>>> x1 = {'foo', 'bar', 'baz'}
>>> x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'})
True
>>> x2 = {'baz', 'qux', 'quux'}
>>> x1 <= x2
False



>>> x1 = {'foo', 'bar'}
>>> x2 = {'foo', 'bar', 'baz'}
>>> x1 < x2
True
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'foo', 'bar', 'baz'}
>>> x1 < x2
False


>>> x1 = {'foo', 'bar', 'baz'}
>>> x1.issuperset({'foo', 'bar'})
True
>>> x2 = {'baz', 'qux', 'quux'}
>>> x1 >= x2
False

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'foo', 'baz', 'qux'}
>>> x1 |= x2
>>> x1
{'qux', 'foo', 'bar', 'baz'}
>>> x1.update(['corge', 'garply'])
>>> x1
{'qux', 'corge', 'garply', 'foo', 'bar', 'baz'}


>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'foo', 'baz', 'qux'}
>>> x1 &= x2
>>> x1
{'foo', 'baz'}
>>> x1.intersection_update(['baz', 'qux'])
>>> x1
{'baz'}


>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'foo', 'baz', 'qux'}
>>> x1 -= x2
>>> x1
{'bar'}
>>> x1.difference_update(['foo', 'bar', 'qux'])
>>> x1
set()

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'foo', 'baz', 'qux'}
>>> 
>>> x1 ^= x2
>>> x1
{'bar', 'qux'}
>>> 
>>> x1.symmetric_difference_update(['qux', 'corge'])
>>> x1
{'bar', 'corge'}


>>> x = {'foo', 'bar', 'baz'}
>>> x.pop()
'bar'
>>> x
{'baz', 'foo'}
>>> x.pop()
'baz'
>>> x
{'foo'}
>>> x.pop()
'foo'
>>> x
set()
>>> x.pop()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    x.pop()
KeyError: 'pop from an empty set'


>>> x = {'foo', 'bar', 'baz'}
>>> x
{'foo', 'bar', 'baz'}
>>> 
>>> x.clear()
>>> x
set()


>>> x = frozenset(['foo', 'bar', 'baz'])
>>> x
frozenset({'foo', 'baz', 'bar'})
>>> len(x)
3
>>> x & {'baz', 'qux', 'quux'}
frozenset({'baz'})
>>> x = frozenset(['foo', 'bar', 'baz'])
>>> x.add('qux')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    x.add('qux')
AttributeError: 'frozenset' object has no attribute 'add'
>>> x.pop()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x.pop()
AttributeError: 'frozenset' object has no attribute 'pop'
>>> x.clear()
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    x.clear()
AttributeError: 'frozenset' object has no attribute 'clear'
>>> x
frozenset({'foo', 'bar', 'baz'})


>>> f = frozenset(['foo', 'bar', 'baz'])
>>> id(f)
56992872
>>> s = {'baz', 'qux', 'quux'}
>>> f &= s
>>> f
frozenset({'baz'})
>>> id(f)
56992152
>>> x1 = set(['foo'])
>>> x2 = set(['bar'])
>>> x3 = set(['baz'])
>>> x = {x1, x2, x3}
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x = {x1, x2, x3}
TypeError: unhashable type: 'set'
>>> x1 = frozenset(['foo'])
>>> x2 = frozenset(['bar'])
>>> x3 = frozenset(['baz'])
>>> x = {x1, x2, x3}
>>> x
{frozenset({'bar'}), frozenset({'baz'}), frozenset({'foo'})}
>>> x = {1, 2, 3}
>>> y = {'a', 'b', 'c'}
>>> 
>>> d = {x: 'foo', y: 'bar'}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d = {x: 'foo', y: 'bar'}
TypeError: unhashable type: 'set'
>>> x = frozenset({1, 2, 3})
>>> y = frozenset({'a', 'b', 'c'})
>>> 
>>> d = {x: 'foo', y: 'bar'}
>>> d
{frozenset({1, 2, 3}): 'foo', frozenset({'c', 'a', 'b'}): 'bar'}
