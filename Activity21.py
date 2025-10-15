name = input("What is your name? --> \t")
isDirty = "cute"
sum = 0

while isDirty == "cute":
    answer = input(f"{name}, Do you want to continue washing?(yes / no)-->\t").lower()
    sum += 1
    if answer == 'yes':
        print("Washing Continues....")
        continue
    else:
        print("Washing stops.....")
        break
print(f"Number of cycle is {sum}")