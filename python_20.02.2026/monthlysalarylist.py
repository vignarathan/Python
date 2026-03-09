months=["January","February","March","April","May","June","July","August","September","October","November","December"]
mbasic=[]
tax=[]
print("***********************************************************")
print("--Please Enter the Basic Salaries of Twelve months--")
print("____________________________________________________________")
for x in range(len(months)):
    print("--",months[x],"--")
    salary=int(input("Enter Salary amount :"))
    mbasic.append(salary)
    print("")
print("____________________________________________________________")
totsalary=0
tottax=0
for x in range(len(mbasic)):
    if mbasic[x]>200000:
        tax[x]=mbasic[x]*0.07
    elif mbasic[x]>150000:
        tax[x]=mbasic[x]*0.05
    elif mbasic[x]>10000:
        tax[x]=mbasic[x]*0.03
    else:
        tax[x]=0
        
    tottax+=tax
    totsalary+=mbasic[x]
print("____________________________________________________________")
 
print("Months \tBasic Salary \tTax")   
for x in range(len(months)):  
    print(months[x],"\t",mbasic[x],"\t",tzx[x])
