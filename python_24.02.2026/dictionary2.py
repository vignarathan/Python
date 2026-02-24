d=[("name","vignarathan"),("age",21),("gender","male")]
print(type(d))
data=dict(d)
print(data)
print(type(data))
print(data["name"])
print(data["age"])
print(data["gender"])
print(data.get("name"))
print(data.get("city"))  #None

