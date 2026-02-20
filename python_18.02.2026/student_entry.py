def printmyname(name1,grade1,age1):
    print(f"Student Name \t: {name1}\nGrade \t\t: {grade1}\nAge \t\t: {age1}")

num=int(input("Number of Students : "))
for x in range(1,num+1):
    print("*******************************")
    name=input("Enter Student Name \t:")
    grade=input("Enter Student's Grade \t:")
    age=input("Enter Student's Age \t:")
    print("________________________________")
    printmyname(name,grade,age)
print("*******************************")
    