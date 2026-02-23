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


