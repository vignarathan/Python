a={1,2,3,4,5}
b={3,5,6,8,9}

c=a.union(b)     #union
print(c)

x=a|b         #union
print(x)

d=a.intersection(b)     #intersection
print(d)

y=a&b
print(y)         #intersection

e=a-b
print(e)         #a difference b

f=b-a
print(f)        #b difference a