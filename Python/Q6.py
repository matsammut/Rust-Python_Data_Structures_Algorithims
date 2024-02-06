def prime(num):
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    elif (num % 2) == 0:
        return False
    elif num == 3:
        return True
    # program checks to see if the number is 0, 1, 2 ,3 or even
    # and returns an appropriate result

    current = 3
    while current < num:
        if (num % current) == 0:
            return False
        else:
            current += 2
    return True


# checks if num is prime

def sieveOfEra(num):
    if num == 0 or num == 1:
        return False
    sieve = []
    start = 2

    while start <= num:
        sieve.append(start)
        start += 1
    # create an array with all the values until the provided number
    element = 0
    p = sieve[element]

    while True:
        iterate = p
        count = 1

        while iterate <= num:
            count += 1
            iterate = count * p
            # iterates through all the multiples
            if iterate in sieve:
                sieve.remove(iterate)
                # removes multiples

        element += 1
        if element >= len(sieve):
            return sieve
            # if the end of the elements is reached then the program stops

        p = sieve[element]
        # the sieve moves to the next element that was not marked to see if the pother elements are multiples of it




# Sieve of Eratosthenes


num = int(input("Please enter a positive integer to check if it is prime\n"))
while num < 0:
    num = int(input("Error integer must be positive please enter again\n"))
check = prime(num)

if check == True:
    print("The number is prime\n")
else:
    print("The number is not prime\n")

primeNums = sieveOfEra(num)

print("Prime numbers until that value \n")
print(primeNums)
