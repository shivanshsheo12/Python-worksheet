# S1 is a set defined as S1= [10, 20, 30, 40, 50, 60]. S2 is a set defined as S2= [40, 50, 60, 70, 80, 90].

S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i) WAP to add 55 and 66 in Set S1.
S1.add(55)
S1.add(66)
print("S1 after adding 55 and 66:", S1)

# (ii) WAP to remove 10 and 30 from Set S1.
S1.discard(10)
S1.discard(30)
print("S1 after removing 10 and 30:", S1)

# (iii) WAP to check whether 40 is present in S1.
is_present = 40 in S1
print("Is 40 present in S1?", is_present)

# (iv) WAP to find the union between S1 and S2.
union = S1.union(S2)
print("Union of S1 and S2:", union)

# (v) WAP to find the intersection between S1 and S2.
intersection = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection)

# (vi) WAP to find the S1 - S2.
difference = S1.difference(S2)
print("Difference between S1 and S2 (S1 - S2):", difference)