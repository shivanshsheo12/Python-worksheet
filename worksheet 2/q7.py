# 7. Write the following program.


# (i) WAP to print 100 random strings whose length between 6 and 8.
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

for _ in range(100):
    length = random.randint(6, 8)
    random_string = generate_random_string(length)
    print(random_string)

# (ii) WAP to print all prime numbers between 600 and 800.
print("Primes between 600 and 800 are")
for num in range (600,800):
    t = num**0.5
    d = 2
    while(d<=t):
        if(num%2==0):
            break
        d+=1
    if(d>t):
        print(num,end=" ")

# (iii) WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9.
for number in range(100, 1001):
    if number % 7 == 0 and number % 9 == 0:
        print(number)