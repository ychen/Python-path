import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

product = operators["*"](4,8)

first_number = int(input("What is the first number? "))

continue_calculation = True

result = first_number

while continue_calculation:

    for operator in operators:
        print(operator)
    operator_to_use = input("Enter operator: ")
    next_number = int(input("What is the next number? "))
    result = operators[operator_to_use](result, next_number)
    print(result)
    continue_or_not = input("Do you want to continue calculation? (y/n): ")

    if continue_or_not == "n":
        continue_calculation = False
        print("See you!")



