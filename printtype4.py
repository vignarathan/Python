#type4
id=1003;
name="Vignarathan"
gr="10A"
ic=200412121313

output="Student ID \t: {}\nStudent Name \t: {}\nGrade Name \t: {}\nNIC No \t\t: {}".format(id,name,gr,ic)
print("-----------------------------")
print("Student Information")
print("-----------------------------")
print(output)
print("-----------------------------")

print("****************************************************")

output="Student ID \t: {0}\nStudent Name \t: {1}\nGrade Name \t: {2}\nNIC No \t\t: {3}".format(id,name,gr,ic)
print("-----------------------------")
print("Student Information")
print("-----------------------------")
print(output)
print("-----------------------------")

print("****************************************************")

output="Student ID \t: {2}\nStudent Name \t: {3}\nGrade Name \t: {1}\nNIC No \t\t: {0}".format(ic,gr,id,name)
print("-----------------------------")
print("Student Information")
print("-----------------------------")
print(output)
print("-----------------------------")

