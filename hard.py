#medium.py

loan = eval(input("Enter loan amount here -->"))
loan_period = eval(input("Enter loan period in years -->"))

months = loan_period * 12
principal = loan / months
balance = loan

print("months\t|\tPrincipal payment|\tRemaining Balance\t|\tInterest\t")

for i in range(1, months +1,1):
    balance -= principal
    interest = balance * 0.03
    monthly = principal + interest
    print(f"{i}\t|\t{round(principal,2)}\t\t|\t{round(balance,2)}\t|\t{round(interest,2)}\t|\t{round(monthly,2)}")
    