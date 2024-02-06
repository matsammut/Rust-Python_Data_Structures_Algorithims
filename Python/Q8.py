while True:
    n = float(input("please enter a positive integer to find its square root\n"))
    if n > 0:
        break
    print("Error: negative integer entered or zero")
    # asks the user for a positive integer and if this isn't met he is asked to reenter

x = n/2
# starts with n being half of x
# this is because square roots greater than 4 are all less than half their squares
i = 0
while True:
    x = (1/2)*(x+(n/x))
    # Newton-Raphson formula
    if x*x == n:
        # if the current approximation square equals the original value then the square root has been achieved
        print('The square root is : ', x)
        break
    if i == 20:
        print('iteration limit reached (20 iterations)')
        print('The approximated square root is : ', x)
        break
    i += 1
# every iteration gives a more accurate approximation

