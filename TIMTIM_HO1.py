cute = input("Enter a word here: ")
word_length = len(cute)
number = []

for i in range(6):
    num = int(input(f"Enter a number here {i + 1}: "))
    number.append(num)

def word_average(number):
    if len(number) == 0:
        return 0
    total = sum(number)
    return total / len(number)

average = word_average(number)

print("The list of the numbers entered is:", number)
print("The length of the word:", word_length)
print("The average of the numbers:", average)

if word_length < average:
    print(f"The length of the word '{cute}' is less than the average.")
elif word_length > average:
    print(f"The length of the word '{cute}' is greater than the average.")
else:
    print(f"The length of the word '{cute}' is equal to the average.")