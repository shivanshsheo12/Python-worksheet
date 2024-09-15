#Write a program that will convert celsius value to Fahrenheit. 

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")