print(r'''hello,\n
world''')

print('''line1
... line2
...line3''')

print("I\'m ok. ")

print("I\'m learning\nPython.")

print("\\\n\\")

print(r"I can try \nthis")

%-------------
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

a=not True
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

print(r"# -*- coding: utf-8 -*-")
n = 123
print("n=",n)
f = 456.789
print("f=",f)
s1 = 'Hello, world'
print("s1=\'",s1,"\"")
s2 = 'Hello, \'Adam\''
print(r"s2 = 'Hello, \'Adam\''")
print("s3 = \'Hello, \"Bart\"\'")
print("s4 = r\'\'\'Hello,")
print("Lisa!\'\'\'")
%--------------