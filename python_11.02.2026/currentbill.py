unit=int(input("Enter Current Usage(in units) :"))

if(unit>300):
    pay=((unit-150))*15+(60*10)+(90*7)
    tax="3%"
    pay=pay+pay*0.03
elif(unit>150):
    pay=((unit-150)*15)+(60*10)+(90*7)
    tax="0%"
elif(unit>90):
    pay=((unit-90)*10)+(90*7)
    tax="0%"
elif(90>=unit>0):
    pay=unit*7
    tax="0%"
    
print("**************************************************")
print("\tCurrent Bill")
print("**************************************************")
print("Usage (in units) \t:",unit)
print("Tax percentage \t\t:",tax)
print("Bill Amount \t\t:",pay)


    
    
  

     
