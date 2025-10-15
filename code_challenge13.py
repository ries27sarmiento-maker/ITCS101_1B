name = input("What is your name?-->\t")
sum = 0
odd = ""
print("ODD NUMBER SUMMARATION, press 0 to stop")

while  True:
    number = eval(input("Enter a number here -->\t"))
    if number == 0:
        print("The program has stop")
        break
    if number %2 == 0: 
        print(f"{number}\t IS AN EVEN NUMBER")
        continue
        

    if number %2 == 1:
        print(f"{number}\t IS AN ODD NUMBER")
        sum += number
        odd += str(number) + " "
        continue
print(f"hi, {name}, The sum off all ODD NUMBER is:\t{sum}")
print(f"ODD numbers detected included the {odd}")




