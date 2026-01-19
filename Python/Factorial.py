# #write a function that returns the factorial of a number using recursion
def fact(f1):
    if f1==1:
        return 1
    else:
        return f1*fact(f1-1)

print("Factorial of 5 is ", fact(5))