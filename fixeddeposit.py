print("************************************************")
print("\t\tYARL Bank")
print("************************************************")
d=int(input("Enter Deposit amount\t:LKR."))
print("________________________________________")
print("---Term Period---")
print("3 Months\tEnter \t1")
print("6 Months \tEnter \t2")
print("1 Year\t\tEnter \t3")
print("3 Years\t\tEnter \t4")
print("5 Years\t\tEnter \t5")
print("________________________________________")

t=int(input("Enter Term Period :"))
print("************************************************")

def calc(depo,rate,term):
    totint=depo*(rate/100)*(term//12)
    matamount=depo+totint
    print("Principle Amount \t\t:",depo)
    print("Fixed Term \t\t\t:",term,"Months")
    print("Annual Interset Rate \t\t:",rate,"%")
    print("Total Interest at Maturity \t:",totint)
    print("Net Amount at Maturity \t\t:",matamount)
    
match t:
    case 1:
        calc(d,5,3)
    case 2:
        calc(d,6,6)
    case 3:
        calc(d,7,12)
    case 4:
        calc(d,8.5,36)
    case 5:
        calc(d,9.5,60)
    case _:
        print("Invalid Inut")
print("************************************************")

     