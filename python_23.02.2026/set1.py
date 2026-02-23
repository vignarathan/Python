s={"maths","science","ict","maths","science"}
print(s)
print(type(s))
print(len(s)) #length is 3

# Unordered
# Unchangeable but can add new value
# Duplicate values are not allowed 
#(Duplicate values are removed by auto)

s.add("tamil")
print(s)  #{'science', 'maths', 'ict', 'tamil'}

s.update(["physics","chemistry","combined_maths"])
print(s)

'''s.add("history","commerce")
print(s)'''             
#can not add multiple values by using "add"

s.remove("ict")
print(s)

s.discard("physics")
print(s)

'''s.remove("health")
print(s)'''         #error will show.

s.discard("health")
print(s)   #there is no error if we give a not inizalaized value

s.pop()
print(s)

s.clear()
print(s)

'''s.pop(2)
print(s)'''        #error will come,because set is unordered


