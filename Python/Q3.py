import random

aSize = random.randint(8, 16)

A = []
Extreme = []

for i in range(aSize):
    A.append(random.randint(0, 128))
# random array is generated

print("Initial array:", A)

n = len(A)
for i in enumerate(A):
    if 0 < i[0] < n - 1 and (A[i[0] - 1] < A[i[0]] > A[i[0] + 1] or A[i[0] - 1] > A[i[0]] < A[i[0] + 1]):
        Extreme.append(A[i[0]])
# each element is checked to see if it meets the condition to be and extreme point
# and if so it is appended to the extreme array

if len(Extreme) > 0:
    print("The extreme points are:")
    print(Extreme)
else:
    print("SORTED")
# Extreme points are printed
# if there aren't any SORTED is printed

# Yes, because the list will be linearly ascending and descending
# (note that one cannot dictate if the list is ascending or descending)