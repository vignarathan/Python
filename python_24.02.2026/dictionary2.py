d=[("name","vignarathan"),("age",21),("gender","male")]
print(type(d))

data=dict(d)
print(data)
print(type(data))

print(data["name"])
print(data["age"])
print(data["gender"])
#print(data["address"])   keyerror:address

print(data.get("name"))
print(data.get("city"))  #there is no error, output:None

