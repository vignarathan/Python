subjects=["Maths","Science","Tamil","ICT","English","History"]
print("***********************************************************")
print(subjects)
print("____________________________________________________________")
print("If you want to change any entry, Enter the new Subject \nIf there are no changes,Please Enter the same again")
print("____________________________________________________________")
for x in range(len(subjects)):
    print("--",subjects[x],"-- ")
    subjects[x]=input("Enter the new Subject : ")
print("____________________________________________________________")
print(subjects)
print("***********************************************************")
