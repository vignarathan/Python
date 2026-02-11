basic=int(input("Enter Basic Salary :"))
per=""
tax=0
net=0
if(basic>0):
    if(basic>=100000):
        per="5%"
        tax=basic*0.05
    elif(basic>=80000):
        per="3%"
        tax=basic*0.03
    else:
        per="0%"
        tax=0
    net=basic-tax
else:
    print("Invalid Input")
    
print("*****************")
print("Basic Salary \t:",basic)
print("Tax Percentage \t:",per)
print("Tax \t\t:",tax)
print("Net Salary \t:",net)
    