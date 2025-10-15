

for i in range(1,6,1):
    for z in range(6,i,-1):
        print(" ", end= "")
    for p in range(1,i*2,1):
        print("*", end="")
    print()

for j in range(1,6,1):
    for m in range(j,7,1):
        print("", end="")
    for g in range(0,j,1):
        print(j, end = "")
    print()