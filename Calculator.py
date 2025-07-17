#Addition function
def add(a, b):
    results = a+b
    return results

#Subtraction Function
def subtract(a, b):
    results = a-b
    return results

#Multiplication Function
def multiply(a, b):
    results =a*b
    return results

#Division Function
def divide(a, b):
    if b == 0:
        print("Error!!Division by Zero is impossible")
    else:
        results =a/b
        return results
    
#Exit Function
def exit():
        if userChoice == 5:
            print("Thank you for using this Calculator.")
        return 0
    
    #List of operations
while True:
    print("===================Simple Operations Calculator==================")
    print("==================== Choose an operation (1-5) ==================")
    print("|\t\t1.Addition\t\t\t\t\t|")
    print("|\t\t2.Subtraction\t\t\t\t\t|")
    print("|\t\t3.Multiplication\t\t\t\t|")
    print("|\t\t4.Division\t\t\t\t\t|")
    print("|\t\t5.Exit\t\t\t\t\t\t|")
    print("=================================================================")

    #Operation Implementation
    userChoice =int(input("Enter your choice:"))
    if userChoice == 1:
        a = float(input("Enter the First Number:"))
        b = float(input("Enter the second Number:"))
        print(f"Results:{a} + {b}=", add(a, b))

    if userChoice == 2:
        a = float(input("Enter the First Number:"))
        b = float(input("Enter the second Number:"))
        print(f"Results:{a} - {b}=", subtract(a, b))

    elif userChoice == 3:
        a = float(input("Enter the First Number:"))
        b = float(input("Enter the second Number:"))
        print(f"Results:{a} * {b}=", multiply(a, b))

    elif userChoice == 4:
        a = float(input("Enter the Numerator:"))
        b = float(input("Enter the Denominator:"))
        print(f"Results:{a} / {b}=", divide(a, b))

    elif userChoice == 5:
        exit()
        break
