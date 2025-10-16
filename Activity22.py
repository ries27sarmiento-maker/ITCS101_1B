import random

print("GUESSING GAME....")
print("+++++++++++++++++\n")

random_value = random.randint(1,100)
tries = 0
goeww = True

while goeww  == True:
	number = eval(input("Guess a random number  from 1-20 -->\t"))
	
	tries += 1
	if number == random_value:
		print("WINNER! SEND GCASH#")
		print(f"random value is {random_value}")
		break
		
	else:
			print("INCORRECT, Try again")
			continue
print(f"You guessed {tries} times")
