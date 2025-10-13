

loan = eval(input("Enter loan amount : "))
loan_period = eval(input("Enter loan loan_period in years : "))

loan_period *= 12
principal = loan / loan_period
balance = loan
interest = 0
print("Payment Schedule")
print("Month|\tMonthly Payment\t|Interest\t|Principal\t|Remaining Loan\t|")

for i in range(1, loan_period + 1,1):
    balance -= principal
    interest = balance * 0.0125
    monthly = interest + principal
    print(f"{i}\t {round(principal,2)} \t\t{round(balance,2)} \t{round(interest),2}")
        #    \t{monthly}")
