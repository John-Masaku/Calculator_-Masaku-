import math #Imports a module containing build in functionse.g.SquareRoot
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
    
#Percentage Function
def percent(a, b):
    if b != 0:
        results =(a/b)*100
        return results
    else:
        print("Error!!Division by Zero is impossible")

history = []

#Save to memory Function
def store_to_memory(entry):
    history.append(entry)

#Show history Function
def show_history():
    if not history:
        print("No saved Calculations found")
        return
    print("===================Previous Calculations========================")
    for entry in history:
        print("|\t",entry," \t\t\t\t\t|")
    print("=================================================================")

    
#Exit Function
def exit():
        if userChoice == 0:
            print("Thank you for using this Calculator.")
        return 0
    
    #List of operations
while True:#True introduces unterminating loop
    print("===================Simple Operations Calculator==================")
    print("==================== Choose an operation (0-8) ==================")
    print("|\t\t1.Addition\t\t\t\t\t|")
    print("|\t\t2.Subtraction\t\t\t\t\t|")
    print("|\t\t3.Multiplication\t\t\t\t|")
    print("|\t\t4.Division\t\t\t\t\t|")
    #Advanced features
    print("|\t\t5.Power(a^b)\t\t\t\t\t|")
    print("|\t\t6.Square Root\t\t\t\t\t|")
    print("|\t\t7.Percentage\t\t\t\t\t|")
    print("|\t\t8.Show History\t\t\t\t\t|")
    print("|\t\t0.Exit\t\t\t\t\t\t|")
    print("=================================================================")

    #Operation Implementation
    userChoice =int(input("Enter your choice:"))
    if userChoice == 1:
        a = float(input("Enter the First Number:"))
        b = float(input("Enter the second Number:"))
        print(f"Results:{a} + {b}=", add(a, b))
        entry = "{a}+{b}=", add(a, b)
        store_to_memory(entry)

    if userChoice == 2:
        a = float(input("Enter the First Number:"))
        b = float(input("Enter the second Number:"))
        print(f"Results:{a} - {b}=", subtract(a, b))
        entry = f"{a} - {b}=", subtract(a, b)
        store_to_memory(entry)

    elif userChoice == 3:
        a = float(input("Enter the First Number:"))
        b = float(input("Enter the second Number:"))
        print(f"Results:{a} * {b}=", multiply(a, b))
        entry = f"{a} * {b}=",multiply(a, b)
        store_to_memory(entry)

    elif userChoice == 4:
        a = float(input("Enter the Numerator:"))
        b = float(input("Enter the Denominator:"))
        print(f"Results:{a} / {b}=", divide(a, b))
        entry = f"{a} / {b}=", divide(a, b)
        store_to_memory(entry)

    elif userChoice == 5:
        a = float(input("Enter the base:"))
        b = int(input("Enter the power:"))
        print(f"Results:{a}^{b}=", math.pow(a, b))
        entry = f"{a} ^ {b}=", math.pow(a, b)
        store_to_memory(entry)

    elif userChoice == 6:
        a = float(input("Enter your number:"))
        print(f"Rusul√ts:{a} =", math.sqrt(a))
        entry =f"√{a}=", math.sqrt(a)
        store_to_memory(entry)

    elif userChoice == 7:
        a =float(input("Enter the part:"))
        b =float(input("Enter the whole:"))
        print(f"Results:{a}=",percent(a, b),f"% of {b}")
        entry = f"{a}/{b} *100 =", percent(a, b),"%"
        store_to_memory(entry)

    elif userChoice == 8:
        show_history()

    elif userChoice == 0:
        exit()
        break #To exit the loop
