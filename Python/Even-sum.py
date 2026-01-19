# #create a program that takes a list of integers & returns the sum of even numbers only
l1=[10,2,3,4,5]
sum=0
for i in l1:
    if i%2==0:
        sum+=i
print("sum of even number in list ",l1, " is ", sum)