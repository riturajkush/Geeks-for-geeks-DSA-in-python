Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "abc"
>>> b = "cab"
>>> r = a[1] + a[2] + a[:1]
>>> r
'bca'
>>> r = a[len-2:] + a[:len-2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    r = a[len-2:] + a[:len-2]
TypeError: unsupported operand type(s) for -: 'builtin_function_or_method' and 'int'
>>> r = a[len(a)-2:] + a[:len(a)-2]
>>> r
'bca'
>>> m = a[2:] + a[:2]
>>> m
'cab'
>>> a = "abc"
>>> b = "bcd"
>>> a-b
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> a+b
'abcbcd'
>>> s = ["a","b"]
>>> str(s)
"['a', 'b']"
>>> s
['a', 'b']
>>> 
======== RESTART: C:/Users/rituraj kushwaha/Desktop/odd even diff.py ========
Traceback (most recent call last):
  File "C:/Users/rituraj kushwaha/Desktop/odd even diff.py", line 10, in <module>
    even = even+digit
NameError: name 'even' is not defined
>>> 
======== RESTART: C:/Users/rituraj kushwaha/Desktop/odd even diff.py ========
4
Traceback (most recent call last):
  File "C:/Users/rituraj kushwaha/Desktop/odd even diff.py", line 14, in <module>
    peint(even)
NameError: name 'peint' is not defined
>>> 
======== RESTART: C:/Users/rituraj kushwaha/Desktop/odd even diff.py ========
4
2
>>> 
======== RESTART: C:/Users/rituraj kushwaha/Desktop/odd even diff.py ========
4
2
>>> 
======== RESTART: C:/Users/rituraj kushwaha/Desktop/odd even diff.py ========
1
0
>>> 
======== RESTART: C:/Users/rituraj kushwaha/Desktop/odd even diff.py ========
1
0
>>> 
======== RESTART: C:/Users/rituraj kushwaha/Desktop/odd even diff.py ========
0
2
>>> a = 129
>>> a = str(129)
>>> a
'129'
>>> if (9 in a):
	print(True)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    if (9 in a):
TypeError: 'in <string>' requires string as left operand, not int
>>> int('a')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int('a')
ValueError: invalid literal for int() with base 10: 'a'
>>> int('1')
1
>>> a = "abcd"
>>> i =0
>>> while(i!=None):
	print(s[i])
	i += 1

	
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    print(s[i])
NameError: name 's' is not defined
>>> while(i!=None):
	print(a[i])
	i += 1

	
a
b
c
d
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    print(a[i])
IndexError: string index out of range
>>> a = '123'
>>> a[0].isdigit()
True
>>> b = ''
>>> int(b)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: ''
>>> 
