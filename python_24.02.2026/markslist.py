student=["Raj","Kamal","Suresh","Nimal","Ramesh"]
subject=["Maths","Science","English"]
marks=[[95,86,75],[93,87,69],[83,72,56],[72,45,63],[97,87,78]]
total=[]
average=[]
result=[]
for x in range(len(student)):
    tot=ave=0
    for y in range(len(subject)):
        tot+=marks[x][y]
    total.append(tot)
    
    ave=tot/len(subject)
    average.append(ave)
    
    if(ave>=80):
        re="Supermerit"
    elif(ave>=70):
        re="Merit"
    elif(ave>=60):
        re="Optimi"
    else:
        re="False"
    result.append(re)

print(f"{'StudentName':<15}{'Maths':<8}{'Science':<10}{'English':<10}{'Total':<8}{'Average':<12}{'Result':<9}")
for x in range(5):
    print(f"{student[x]:<15}",end="")
    for y in range(3):
        print(f"{marks[x][y]:<10}",end="")
    print(f"{total[x]:<8}{average[x]:<10,.2f}{result[x]:<5}")