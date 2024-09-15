#WAP to find compound interest for given values. 

P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (as a percentage): ")) / 100
n = int(input("Enter the number of times interest is compounded per year: "))
t = float(input("Enter the number of years the money is invested or borrowed for: "))

A = P * (1 + r / n) ** (n * t)
CI = A - P
print(f"Final Amount: {A:.2f}")
print(f"Compound Interest: {CI:.2f}")