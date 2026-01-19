#write a program that prints the first 10 fibonacci numbers using while loop
count=0
a=0
b=1
print(a)
print(b)
while count<8:
    c=a+b
    print(c)
    a=b
    b=c
    count+=1