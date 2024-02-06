while True:
    n = int(input("Till which integer in the fibonacci sequence? \n"))
    if n > 2:
        break
    print("Error integer must be greater than 2 in a fibonacci sequence")
    # the user is asked for the number of terms he wishes and is asked to re-enter if the integer is less than 3

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    # function that returns the fibonacci number at n terms

count = 0
sum = 0
limit = n
while True:
    if count == n:
        break
    sum += fibonacci(limit)
    limit -= 1
    count += 1
# loops adding the fibonacci number each time to the sum

print("The sum of the Fibonacci sequence is :", sum)
# sum is printed and the program terminates
