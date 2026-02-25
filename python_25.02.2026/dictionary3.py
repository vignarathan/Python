d={"name":"vignarathan","age":21,"gender":"male"}
key=d.keys()
print(key)

value=d.values()
print(value)
print("********************************")
for key,value in d.items():
    print(f"{key}\t{value}")
print("********************************")
for key in d.keys():
    print(key)
print("********************************")
for value in d.values():
    print(value)