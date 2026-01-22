
# # Build a calculator function that accepts any number of inputs.Support add, subtract, multiply via keyword flag.
def calculator(*numbers, operation="add"):
    if not numbers:
        return "No numbers provided"

    if operation == "add":
        result = 0
        for num in numbers:
            result += num
        return result

    elif operation == "subtract":
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result

    else:
        return "Invalid operation"
print(calculator(1,2,3,operation="add"))
                
