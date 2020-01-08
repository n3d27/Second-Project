while True:

    print("Option")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two number")
    print("Enter 'multiply' to multiply two number")
    print("enter 'divide' to divide two number")
    print("Enter 'quit' to end the program")
    user_input = input (": ")
    
    if user_input == "quit":
        break
    if user_input =="add":
        ...
    if user_input =="subtract":
        ...
    if user_input =="multiply":
        ...
    if user_input =="divide":
        ...
    else:
        print("Unknown input")
    if user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)

    if user_input =="subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is " + result)
    
    if user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is " + result)

    if user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("The answer is " + result)
        
