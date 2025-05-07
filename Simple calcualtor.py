while True:
    operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")
    
    if operator == "q":
        print("Exiting the calculator. Goodbye!")
        break
    elif operator in ["+", "-", "*", "/"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operator == "+":
            print("The Answer is", a + b)
        elif operator == "-":
            print("The Answer is", a - b)
        elif operator == "*":
            print("The Answer is", a * b)
        elif operator == "/":
            if b != 0:
                print("The Answer is", a / b)
            else:
                print("Cannot divide by 0")
    else:
        print("Invalid operator")


    
    
