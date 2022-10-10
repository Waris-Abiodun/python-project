name = 'Waris Abiodun'
age = 90
print(name, age)
print('\n')
#Basic Calculator
num1, operator,num2 = input("Enter the your arithemetic calculation(use ^ fot raise to power and normal signs for others) : ").split(' ')
num1 = int(num1)
num2 = int(num2)
if (operator == '+'):
    ans = num1 + num2
    print(num1, "+", num2, '=', ans)
elif (operator == '-'):
    ans = num1 - num2
    print(num1, "-", num2, '=', ans)
elif (operator == '*'):
    ans = num1 * num2
    print(num1, "*", num2, '=', ans)
    
elif (operator == '/'):
    if(num2 == 0):
        print("undefined")
    else:
        ans = num1 // num2
        print(num1, "/", num2, '=', ans)
elif (operator == '%'):
    if(num2 == 0):
        print("Hey, You cant use 0 has modulo")
    else:
        ans = num1 % num2
        print(num1, "%", num2, '=', ans)
elif (operator == '^'):
     print(num1, "^", num2, '=', num1**num2)
else:
    print('invalid sign!!!, You can only add , subtract,multyiply, find exponent,divide and find remainder')


#for loop
for y in range (10, 20): #start, stop ,step
    print(y)

#while loop
y = 0
while (y <= 10):
    print(y)
    y = y + 1

stop = "false"
while (stop != "stop"):
    stop = input("input a sentence, you can use 'stop' to stop the prompt ")
    print(stop)
    
   
