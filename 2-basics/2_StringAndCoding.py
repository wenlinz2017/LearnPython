# -*- coding: utf-8 -*-

print("包含中文的str")
ord("林")
chr("31415")
'\u4e2d\u6587'

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

a = "Arttutor"
b = 19
print("%s provides a monthly subscription of $%d only." % (a,b))

print(ord("B"))

print(len("Facts become stories, and stories become legends."))

s1=72
s2=85
r = (s2-s1)/s1
print(r)
print('Hello, {0}, your score has improved by {1:.1f}%.'.format("Xiaoming", r))