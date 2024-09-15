#D is a dictionary defined as D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}.

D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

# (i) WAP to add new entry in D; key=8 and value is 8.8
D[8] = 8.8
print(D)

# (ii) WAP to remove key=2.
if 2 in D:
    del D[2]
print(D)

# (iii) WAP to check weather 6 key is present in D.
key_to_check = 6
is_present = key_to_check in D
print(is_present)

# (iv) WAP to count the number of elements present in D.
count = len(D)
print(count)

# (v) WAP to add all the values present D.
total_sum = 0
for value in D.values():
    total_sum += value
print(total_sum)

# (vi) WAP to update the value of 3 to 7.1.
if 3 in D:
    D[3] = 7.1
print(D)

# (vii) WAP to clear the dictionary.
D.clear()
print(D)