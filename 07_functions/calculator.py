n1 = float(input("Enter A Number: "))
n2 = float(input("Enter Another Number: "))
choose_operation = input("Choose An Operation (+, -, *, /): ")
def calculate(n1, n2, operation):
    if operation == '+':
        return n1 + n2
    elif operation == '-':
        return n1 - n2
    elif operation == '*':
        return n1 * n2
    elif operation == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

result = calculate(n1, n2, choose_operation)
print("Result:", result)
