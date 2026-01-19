# #use a for loop with break to find the first number divisible by both 5 and 7 in a list.
l1=[10,2,15,35,21]
for i in l1:
    if i%5==0 and i%7==0:
        break
    else:
        print(i)