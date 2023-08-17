from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symblo = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        calculator_function = operations[operation_symblo]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symblo} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or"
                 f"type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            calculator()


calculator()
