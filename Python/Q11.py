import math

cos = 0
while True:
    equation = input("Please enter the equation in the form 'sin63' or 'cos4'\n")
    if equation[0:3] == "sin":
        print("Sin value entered\n")
        break
    elif equation[0:3] == "cos":
        print("Cos value entered\n")
        cos = 1
        break
    # checks to see if sine or cosine was entered
    else:
        print("Error neither sine or cosine entered please re enter in the correct format\n")
    # if the user entered neither sine or cosine, the equation is re-entered

x = int(equation[3:]) #x value
counter = 0
ans = 0
n = int(input("For how many times do you wish the program to loop through (n times) \n"))

while counter != n:
    if cos == 0:
        ans += (((-1)**counter)/math.factorial(2*counter+1))*(x**(2*counter+1))
        # this formula is utilised if the user entered sin
    else:
        ans += (((-1) ** counter) / math.factorial(2 * counter)) * (x ** (2 * counter))
        # this formula is utilised if the user entered cos
    counter += 1
# the program loops for n times

print(ans)
