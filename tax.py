basic=int(input("Enter Basic Salary :"))
per=""
tax=0
net=0
if(basic>0):
    if(basic>=100000):
        per="5%"
        tax=basic*0.05
        net=basic-tax
    elif(basic>=80000):
        per="3%"
        tax=basic*0.05
        net=basic-tax
    else:
        per="0%"
        net=basic
        net=basic
else:
    print("Invalid Input")
    
    
print("*****************")
print("Basic Salary \t:",basic)
print("Tax Percentage \t:",per)
print("Tax \t\t:",tax)
print("Net Salary \t:",net)
    