import random

asize = random.randint(256, 1024)
bsize = random.randint(256, 1024)
# generate the size of each array

A = []
B = []

while asize == bsize:
    bsize = random.randint(256, 1024)
# if both arrays are the same size array B is reset

for i in range(asize):
    A.append(random.randint(0, 1024))

for i in range(bsize):
    B.append(random.randint(0, 1024))
# both arrays are populated

print("Array Before Shell Sort: ", A)
print("Array Before Quick Sort: ", B)

# shell sort
gap = asize // 2
while gap > 0:
    for index in enumerate(A[gap:]):

        if A[index[0]] > A[gap + index[0]]:
            hold = A[index[0]]
            A[index[0]] = A[gap + index[0]]
            A[gap + index[0]] = hold
    gap = gap // 2
# insertion sort
for index in enumerate(A[0:]):
    temp = index[1]
    aIndex = index[0] - 1
    aValue = index[0]
    while aIndex >= 0 and temp < A[aIndex]:
        A[aValue] = A[aIndex]
        aIndex -= 1
        aValue -= 1
    A[aIndex + 1] = temp


# quick sort
def pivotpos(B, first, last):
    # choose pivot using first middle last
    pvot = last - 1
    # sort first last and middle
    if B[last] < B[pvot]:
        hold = B[last]
        B[last] = B[pvot]
        B[pvot] = hold
    elif B[pvot] > B[last]:
        hold = B[pvot]
        B[pvot] = B[last]
        B[last] = hold
    if B[pvot] < B[first]:
        hold = B[pvot]
        B[pvot] = B[first]
        B[first] = hold

    # swap pivot with last value
    hold = B[pvot]
    B[pvot] = B[last]
    B[last] = hold
    # set i and j to starting positions
    left = first
    # -1 because otherwise right would be the pivot
    right = last - 1
    while True:
        # i moving until it finds a value greater than the pivot
        while B[left] < B[last]:
            left += 1
        while B[right] >= B[last] and right != 0:
            right -= 1
        # when i passes j, swap i with the pivot and stop
        if left > right or right == 0:
            hold = B[left]
            B[left] = B[last]
            B[last] = hold
            break
        # swapping i and j
        hold = B[left]
        B[left] = B[right]
        B[right] = hold
    return left

def quickSort(B, first, last):
    if last < first+1:
        return B
    middle = pivotpos(B, first, last)
    # rearrange
    quickSort(B, first, middle-1)
    quickSort(B, middle+1, last)


quickSort(B, 0, bsize-1)
print("Array After Shell Sort: ", A)
print("Array After Quick Sort: ", B)

i = 0
j = 0

C = []

# merge sort
while i < asize and j < bsize:
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

# remaining elements are added
while i < asize:
    C.append(A[i])
    i += 1
while j < bsize:
    C.append(B[j])
    j += 1

print("Array of both Arrays merged in linear time: ", C)