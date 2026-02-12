x=int(input("Enter Number1 : "))
y=int(input("Enter Number2 : "))
print("***********************************")
print("For Addition \t\tEnter \t1")
print("For Subtraction \tEnter \t2")
print("For Multiplication \tEnter \t3")
print("For Division \t\tEnter \t4")
print("***********************************")
op=int(input("Enter Arithmetic Function :"))

match op:
    case 1:
        print(x,"+",y,"=",x+y)
    case 2:
        print(x,"-",y,"=",x-y)
    case 3:
        print(x,"*",y,"=",x*y)
    case 4:
        print(x,"/",y,"=",x/y)
    case _:
        print("Invalid input")

