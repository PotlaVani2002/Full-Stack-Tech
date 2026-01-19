#create a calculator that performs basic all arthimetic operations based on user input.
def calculator(a, b, op):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return "Error" if b == 0 else a / b
        case "%":
            return "Error" if b == 0 else a % b
        case "//":
            return "Error" if b == 0 else a // b
        case "**":
            return a ** b
        case _:
            return "Invalid operation"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation: ")
print("Result:", calculator(num1, num2, op))