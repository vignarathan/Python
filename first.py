Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Vignarathan")
Vignarathan
>>> name="Vignarathan"
>>> print(name)
Vignarathan
>>> print("name")
name
>>> print('name')
name
>>> type(name)
<class 'str'>
>>> name=10
>>> type(name)
<class 'int'>
>>> name="10"
>>> type(name)
<class 'str'>
>>> print('10')
10
>>> name=vikki
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name=vikki
NameError: name 'vikki' is not defined
>>> id=1003
>>> name="vikki"
>>> age=21
>>> print("my name is",id)
my name is 1003
>>> print("my name is",name)
my name is vikki
>>> print("my age is",age)
my age is 21
>>> print("my id is",id)
my id is 1003
>>> print("my name is"+name)
my name isvikki
>>> print("my name is "+name)
my name is vikki
>>> 1003=id
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> print("my age is "+str(age))
my age is 21
>>> print("my name is",name,"my age is",age,"my id is",id)
my name is vikki my age is 21 my id is 1003
print("my name is",name,"\n","my id is",id,"\n","my age is",age)
my name is vikki 
 my id is 1003 
 my age is 21
print("my name is",name,"\nmy id is",id,"\nmy age is",age)
my name is vikki 
my id is 1003 
my age is 21
