num1, num2 = input("Enter a number: "), input("Enter a number: ")
operation = input("Enter an operation (div/mul/add/sub): ")
ok = False

try:
    num1 = int(num1)    
    try:
        num2 = int(num2)
        if operation == "add": print(num1 + num2)
        elif operation == "mul": print(num1 * num2)
        elif operation == "sub": print(num1 - num2)
        elif operation == "div": 
            try:
                print(num1 / num2)
            except: print("Sorry, a division by zero is impossible.")
        else:
            print("I don't know this operation!")
    except: 
        print("Sorry, the second number you entered is not a number.")
        ok = True
except: print("Sorry, the first number you entered is not a number.")