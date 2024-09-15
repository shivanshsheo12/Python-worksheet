# 1. L is a list defined as L= [11, 12, 13, 14].

# (i) WAP to add 50 and 60 to L.
L = [11, 12, 13, 14]
additional_elements = [50, 60]
for elem in additional_elements:
    L += [elem]
print(L)


# (ii) WAP to remove 11 and 13 from L.
to_remove = [11, 13]
new_list = []
for item in L:
    if item not in to_remove:
        new_list.append(item)
L = new_list
print(L)  # Output: [12, 14, 50, 60]


# (iii) WAP to sort L in ascending order.
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
print(L)

# (iv) WAP to sort L in descending order.
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] < L[j]:
            L[i], L[j] = L[j], L[i]
print(L)

# (v) WAP to search for 13 in L.
search_value = 13
found = False
for item in L:
    if item == search_value:
        found = True
        break
print(found)

# (vi) WAP to count the number of elements present in L.
count = 0
for _ in L:
    count += 1
print(count)

# (vii) WAP to sum all the elements in L.
total_sum = 0
for item in L:
    total_sum += item
print(total_sum) 

# (viii) WAP to sum all ODD numbers in L.
odd_sum = 0
for item in L:
    if item % 2 != 0:
        odd_sum += item
print(odd_sum)

# (ix) WAP to sum all EVEN numbers in L.
even_sum = 0
for item in L:
    if item % 2 == 0:
        even_sum += item
print(even_sum)

# (x) WAP to sum all PRIME numbers in L.
prime_sum=0
for num in L:
    t = num**0.5
    d = 2
    while(d<=t):
        if(num%2==0):
            break
        d+=1
    if(d>t):
        prime_sum+=num

# (xi) WAP to clear all the elements in L.
L = []
print(L)

# (xii) WAP to delete L.
del L