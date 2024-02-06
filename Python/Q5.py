RPN = []
Stack = []

sPOS = 0
hold = ""
# declaration of variables

print("Enter the reverse polish notation to calculate it\n")
temp = input("Note: put commas between the numbers/symbols example 3,10,5,+,*,\n")
for letters in temp:
    if letters == ',':
        RPN.append(hold)
        hold = ""
    else:
        hold += letters
print(RPN)
# tokenisation of input

if hold != "":
    RPN.append(hold)


for i in enumerate(RPN):
    if i[1] == '*':
        Stack[sPOS-2] = int(Stack[sPOS-2])*int(Stack[sPOS-1])
        Stack.pop(sPOS-1)
        sPOS -= 1
    elif i[1] == '/':
        Stack[sPOS-1] = int(Stack[sPOS-2])/int(Stack[sPOS-1])
        sPOS -= 1
    elif i[1] == '-':
        Stack[sPOS-1] = int(Stack[sPOS-2])-int(Stack[sPOS-1])
        sPOS -= 1
    elif i[1] == '+':
        Stack[sPOS-2] = int(Stack[sPOS-2])+int(Stack[sPOS-1])
        Stack.pop(sPOS - 1)
        sPOS -= 1
    else:
        Stack.append(i[1])
        sPOS += 1
    # arithmetic  operations
    print("Contents Currently of the Stack :\n")
    print(Stack)
