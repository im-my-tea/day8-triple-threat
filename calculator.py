import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.calc_logo)

def calculator():
    n1 = float(input("Enter first number: "))
    c = 1
    while c:
        for i in operations:
            print(i)
        operation = input("Enter operation: ")
        n2 = float(input("Enter second number: "))
        if operation not in operations:
            print("Invalid operation, choose again.\n")
            continue
        t = operations[operation](n1, n2)
        print(f"Operation: {n1} {operation} {n2},   Result: {t:.2f}")
        c = int(input("Do you want to continue with same number? (yes - 1/no - *): "))
        if c != 1:
            x = int(input("Do you want to start again? (yes - 1/no - *): "))
            if x != 1:
                print("Goodbye!")
                break
            else:
                calculator()
        else:
            n1 = t
            c = 1
            continue

calculator()

        