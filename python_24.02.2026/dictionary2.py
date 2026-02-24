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
print(data.get("city","jaffna"))  #if key is not there can add a value as default


data["NIC"]=200565487896
print(data)

data.update({"age":23,"NIC":200789654563})
print(data)

del data["name"]
print(data)

data.pop("age")
print(data)

data.popitem()
print(data)

data.clear()
print(data)
