uname="YarlIT"
pw="Yit@2026"
role=""

iuname=input("Enter Username : ")
ipw=input("Enter Password : ")
irole=input("Enter Your Role(admin or student): ")

if((iuname==uname) and (ipw==pw)):
    if(irole=="admin"):
        print("Welcome To Admin DashBoard")
    elif(irole=="student"):
        print("Welcome To Student DashBoard")
    else:
        print("Invalid Role")
else:
    print("Invalid Username or Password")