# #create a loop that prints numbers from 1 to 50 ,skipping multiples of 3
for i in range(1,51):
    if i%3==0:
        continue
    else:
        print(i)