list=[2,3,45,5,7,8,4]
print(list)
for i in list:
    print(i)
for i in range(0,10,2):
    print(i)

    
for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()
    
movies=["war","RRR","puspha"]
i=0
while i<len(movies):
    print(movies[i])
    i+=1
i=0
while i>6:
    print("*",end="")