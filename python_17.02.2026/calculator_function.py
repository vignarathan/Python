x=int(input("Enter Number1 ="))
y=int(input("Enter Number2 ="))
print("***********************************")
print("For Addition \t\tEnter \t1")
print("For Subtraction \tEnter \t2")
print("For Multiplication \tEnter \t3")
print("For Division \t\tEnter \t4")
print("***********************************")
op=int(input("Enter Arithmetic Function :"))

def addition():
    print(x,"+",y,"=",x+y)

def subtraction():
    print(x,"-",y,"=",x-y)
    
def multiplication():
    print(x,"*",y,"=",x*y)

def division():
    if((y==0) and (x==0)):
        print("Undefinded")
    elif(y==0):
        print("Infinity")
    else:
        print(x,"/",y,"=",x/y)
            
match op:
    case 1:
        addition()
    case 2:
        subtraction()
    case 3:
        multiplication()
    case 4:
        division()
    case _:
    print("Invalid Input")
        
    
        
        
        
        
        
        
        
        