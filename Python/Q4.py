import random

asize = random.randint(64, 128)

A = []

for i in range(asize):
    A.append(random.randint(0, 1024))
# an array is made randomly similar to previous questions

hash = []
ans = []

print(A)

for i in A:
    for j in A:
        if i != j:
            t = (i, j, i*j)
            hash.append(t)
# each element is paired with every other element along with their product (element 1, element 2 , product)

for i in hash:
    for j in hash:
        if i[2] == j[2]:
        # checks if two tuples have the same product
            if i[0] != i[1] and j[0] != j[1] and i[0] != j[1] and j[0] != i[1] and i[0] != j[0] and i[1] != j[1]:
            # checks that both tuples have unique elements so a!=b!=c!=d
                holdAB = (i[0], i[1])
                holdCD = (j[0], j[1])
                holdANS = (holdAB, holdCD)
                ans.append(holdANS)
                # the tuples are tupled and added to the answer list

print("Two pairs of integers: \n")
print(ans)