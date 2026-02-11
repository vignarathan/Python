d1="Monday"
d2="Tuesday"
d3="Wednesday"
d4="Thursday"
d5="Friday"
d6="Saturday"
d7="Sunday"

x=int(input("Enter the number : "))
if(7>=x>=0):
    if(x==1):
        print(d1)
    elif(x==2):
        print(d2)
    elif(x==3):
        print(d3)
    elif(x==4):
        print(d4)
    elif(x==5):
        print(d5)
    elif(x==6):
        print(d6)
    elif(x==7):
        print(d7)
else:
    print("Invalid Input")