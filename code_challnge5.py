total_odd_sum = 0

for i in range(7):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        total_odd_sum += num

print("The sum of all odd numbers is", total_odd_sum)
