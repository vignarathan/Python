months=["January","February","March","April","May","June","July","August","September","October","November","December"]
mbasic=[]
print("***********************************************************")
print("--Please Enter the Basic Salaries of Twelve months--")
for x in range(len(months)):
    mbasic[x]=int(input(months[x],"\t:"))
