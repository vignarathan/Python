student=["Raj","Kamal","Suresh","Nimal","Ramesh"]
subject=["Maths","Science","English"]
marks=[
        [95,86,75],
        [93,87,69],
        [83,72,56],
        [72,45,63],
        [97,87,78]
       ]
       
total=[]
average=[]
result=[]

for x in range(5):
    for y in range(3):
        total[x]+=marks[x][y]
    
print(total)
