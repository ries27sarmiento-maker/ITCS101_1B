name = input("What is your name ? ---> ")
fare = eval(input("Fare free --->"))
isStudent = input("Are you currently a student (yes / no) ")

if isStudent == 'yes' :
	discount = fare * 0.2
	new_fare = fare - discount
	print("Hi", name)
	print("Your discount is ", discount)
	print("Your new fare is ", new_fare)
else:
	print("Sorry ", name, "You are not eligible for a student discount")