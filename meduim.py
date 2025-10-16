number = eval(input("Enter your number here -->"))

rows = 10

for i in range(1, rows + 1):
	for z in range(1, number + 1):
		print(f"{i} x {z} = {i*z}", end= "\t")
	print()


for i in range(1,7,1):
	for z in range(7,i,-1):
		print(" ", end=  "")
	for x in range(1,i + 1, 1):
		print("* ",end=  "")
	print()