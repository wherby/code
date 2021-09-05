#!/usr/bin/python
# -*- coding: utf-8 -*-

a= '''一、主营业务收入
少数股东损益'''

b = a.split()
b = map(lambda x: "\""+x + "\"",b)
#print unicode(a, "utf-8")

d = ",".join(b)
print unicode(d, "utf-8")