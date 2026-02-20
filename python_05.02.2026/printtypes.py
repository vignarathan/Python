id=1003
name="Vignarathan"
age=21

#type1
print("my id is",id)
print("my name is",name)
print("my age is",age)
print("**************")

print("my id is "+str(id))
print("my name is "+name)
print("my age is "+str(age))
print("*****************************")

#type2
print("my id is",id,"\nmy name is",name,"\nmy age is",age)
print("*****************************")

#type3
output=f"my id is {id}\nmy name is {name}\nmy age is {age}"
print(output)
print("*****************************")

#type4
output="my id is {}\nmy name is {}\nmy age is {}".format(id,name,age)
print(output)
print("*************")

output="my id is{0}\nmy name is{1}\nmy age is{2}".format(id,name,age)
print(output)
print("*************")

output="my id is {1}\nmy name is {2}\nmy age is {0}".format(age,id,name)
print(output)
print("*****************************")

#type5
print("my id is %d \nmy name is %s \nmy age is %d"%(id,name,age))
#here %s refers to string and %d refers to int