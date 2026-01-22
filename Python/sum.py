
# How to find the sum of numbers until 0 is entered on the keyboard on Python?
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Sum of numbers:", total)
