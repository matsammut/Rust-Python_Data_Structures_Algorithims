listNum = [2, 3, 1, 6, 2, 1]

largest = -999
pointer = 0

def largestFind(large, listNum, pointer):
    if large < listNum[pointer]:
        large = listNum[pointer]
    # if the current number is larger than the previous larger than the previous than it is set as the new largest

    if pointer == (len(listNum) - 1):
        # if the end of the array is reached then return the current largest value
        return large
    else:
        pointer += 1
        return largestFind(large, listNum, pointer)

hold = largestFind(largest, listNum, pointer)
print(hold)
# print the largest number
