listNum = [2, 3, 1, 6, 2, 4, 1, 2, 5, 7, 3, 3, 3]
listDup = []
# pre-set array made on purpose with duplicate values

largest = -999
smallest = 999

for num in listNum:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    # the largest and smallest values in the array are found

if smallest > 0:
    i = 0
    smallest = 0
else:
    i = smallest
# sets i and smallest to 0

while True:
    listDup.append(0)
    if i >= largest:
        break
    i += 1
    # blank array of the size of the largest value is made

for num in enumerate(listNum):
    listDup.insert(num[1] - smallest, listDup[num[1] - smallest] + 1)
    listDup.pop((num[1] - smallest) + 1)
    # uses the value in the pre-set array as the index to be incremented in the new duplicate array

print(listDup)

for num in enumerate(listDup):
    if listDup[num[0]] > 1:
        print(num[0] + smallest)
# if an element has a value greater than 1 that means it has appeared more than 1 time and
# so should be printed
