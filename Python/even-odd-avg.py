
# How to find the average of odd and even averages of whole numbers on Python?
even_sum = odd_sum = 0
# odd_sum = 0
even_count = 0
odd_count = 0
while True:
    num = int(input("Enter a whole number (0 to stop): "))
    if num == 0:
        break
    if num % 2 == 0:
        even_sum += num
        even_count += 1
    else:
        odd_sum += num
        odd_count += 1
        
if even_count > 0:
    even_avg = even_sum / even_count
else:
    even_avg = 0
if odd_count > 0:
    odd_avg = odd_sum / odd_count
else:
    odd_avg = 0
print("Average of even numbers:", even_avg)
print("Average of odd numbers:", odd_avg)

